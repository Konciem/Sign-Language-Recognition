import cv2

print("wlaczamy okienko")

#init kamery

camera = cv2.VideoCapture(0)
x =0
while True:

    sukces, obraz = camera.read()

    if not sukces:
        print("nie udalo sie!!!")
        break

    obraz_flipped = cv2.flip(obraz, 1)

    cv2.imshow("okienko", obraz_flipped)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()
print("Program zakończony.")