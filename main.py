import cv2

print("Uruchomienie programu")

camera = cv2.VideoCapture(0)
while True:

    success, frame = camera.read()

    if not success:
        print("nie udalo sie!!!")
        break

    frame_flipped = cv2.flip(frame, 1)

    cv2.imshow("okienko", frame_flipped)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()
print("Program end")