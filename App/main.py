import cv2
import mediapipe as mp

print("Start")
camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        print("nie udalo sie!!!")
        break

    frame_flipped = cv2.flip(frame, 1)
    image_rgb = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)

    cv2.imshow("Sign Language", image_rgb)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()
print("End")