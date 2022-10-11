import cv2
import pickle
import cvzone
import numpy as np
from collections import defaultdict

from ParkingSpacePicker import temps
# Video feed
cap = cv2.VideoCapture('carPark_Reverse.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

with open('UniqueID', 'rb') as f:
    UniqueID = pickle.load(f)

width, height = 107, 48

counter = set()
colorBlack = (0, 0, 0)


def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y + height, x:x + width]
        # cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 255, 0)  # GREEN
            thickness = 3
            spaceCounter += 1
            if temps[pos] not in counter:
                counter.add(temps[pos])
                print("Empty at ", temps[pos])

        else:
            color = (0, 0, 255)  # RED
            thickness = 3
            if temps[pos]  in counter:
                counter.remove(temps[pos])

        cv2.rectangle(img, pos, (pos[0] + width,
                      pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                           thickness=1, offset=0, colorR=colorBlack)
        if temps[pos] in counter:
            cvzone.putTextRect(img, "Free", (x+width-40, y + height-34), scale=1,
                               thickness=1, offset=0, colorR=colorBlack)
        else:
            cvzone.putTextRect(img, "Parked", (x+width-60, y + height-34), scale=1,
                               thickness=1, offset=0, colorR=colorBlack)
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                       thickness=5, offset=20, colorR=(0, 200, 0))


while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(
        imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)

    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    cv2.imshow("Image", img)
    #cv2.imshow("ImageBlur", imgBlur)
    #cv2.imshow("ImageThresh", imgThreshold)
    #cv2.imshow("ImageMed", imgMedian)
    #cv2.imshow("imgDilate", imgDilate)
    if cv2.waitKey(1) & 0xFF == ord('d'):  # 0xFF is used to check if the key is pressed
        print("Empty are :", counter)
        break
