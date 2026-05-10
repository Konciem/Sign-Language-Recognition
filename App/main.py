import cv2
import mediapipe as mp

print("Start")
camera = cv2.VideoCapture(0)


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
while True:

    success, frame = camera.read()

    if not success:
        print("nie udalo sie!!!")
        break

    frame_flipped = cv2.flip(frame, 1)
    image_rgb = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame_flipped, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Sign Language", frame_flipped)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()
print("End")