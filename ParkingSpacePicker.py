
import cv2
import pickle

width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

try:
    with open('CarParkPos2', 'rb') as f:
        posDict = pickle.load(f)
except:
    posDict = {}

k = 0


def mouseClick(events, x, y, flags, params):
    global k
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
        
        
        posDict[k] = [(x, y)]
        k+=1
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)
    with open('CarParkPos2', 'wb') as f:
        pickle.dump(posDict, f)


while True:
    img = cv2.imread('carParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width,
                      pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    if cv2.waitKey(10) & 0xFF == ord('d'):  # 0xFF is used to check if the key is pressed
        print(len(posDict))
        for i, pos in enumerate(posDict):
            print(i, pos)
        break
