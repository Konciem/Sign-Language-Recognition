from flask import Flask, render_template, Response, jsonify
from stabilizer import GestureStabilizer
from WordStateMachine import WordStateMachine
import mediapipe as mp
import cv2
import pickle

app = Flask(__name__)

with open("../NoteBooks/asl_model.pkl", "rb") as f:
    model = pickle.load(f)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

camera = cv2.VideoCapture(0)

stabilizer = GestureStabilizer(window_size=15)
word_machine = WordStateMachine()  # Inicjalizacja maszyny stanów

current_state = {
    "char": "---",
    "word": "---"
}


def generate_frames():
    global current_state
    while True:
        success, frame = camera.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        predicted_char = ""
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                data_aux = []
                for lm in hand_landmarks.landmark:
                    data_aux.extend([lm.x, lm.y, lm.z])

                prediction = model.predict([data_aux])
                predicted_char = prediction[0]

        stable_char = stabilizer.get_stable_prediction(predicted_char)

        word_machine.process(stable_char)

        # Aktualizujemy stan globalny
        current_state["char"] = stable_char if stable_char else "---"
        current_state["word"] = word_machine.get_current_word() if word_machine.get_current_word() else "---"

        cv2.putText(frame, stable_char, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/get_data')
def get_data():
    return jsonify(current_state)



@app.route('/reset', methods=['POST'])
def reset_word():
    global current_state
    word_machine.reset()
    current_state["word"] = "---"
    return jsonify({"status": "success", "message": "Zresetowano stan maszyny stanów"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)