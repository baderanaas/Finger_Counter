import cv2
import time
import os
import HandTracking as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "images"
myList = os.listdir(folderPath)
overlayList = []
for imPath in myList:
    image = cv2.imread(f"{folderPath}/{imPath}")
    overlayList.append(image)

pTime = 0

detector = htm.HandDetector(detectionCon=0.75)

while True:
    success, img = cap.read()
    img = detector.findHands(img)

    h, w, c = overlayList[0].shape
    img[0:h, 0:w] = overlayList[0]

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        img, f"FPS: {int(fps)}", (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3
    )

    cv2.imshow("Image", img)
    cv2.waitKey(1)
