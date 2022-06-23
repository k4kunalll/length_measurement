from utils import *

scale = 3

img = cv2.imread("box3.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (700,700))

imgCont, cont = getContours(img, draw=True, filter=4, minArea = 2000)
if len(cont) != 0:
    biggest = cont[0][2]
    # print(biggest)
    imgWarp = wrapImg(img, biggest, 500, 500)

    imgCont2, cont2 = getContours(imgWarp, draw=True, filter=4, cThresh=[100,100], minArea = 500, showCanny = True)

    if len(cont) != 0:
        for obj in cont2:
            cv2.polylines(imgCont2, [obj[2]], True, (0,255,0), 2)
            nPoints = reorder(obj[2])
            mW = round(findDis(nPoints[0][0]//scale, nPoints[1][0]//scale),1)
            nH = round(findDis(nPoints[0][0]//scale, nPoints[2][0]//scale),1)
            print(mW, nH)
            x,y,w,h = obj[3]

            cv2.putText(imgCont2, f"{mW}cm", (x+30, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            cv2.putText(imgCont2, f"{mW}cm", (x-70, y+h//2), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)


    cv2.imshow("imgWarp", imgWarp)


cv2.imshow("Original", img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
