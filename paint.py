import cv2
import numpy as np 

drawing=False
mode=True
ix=-1
iy=-1
def draw(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img,(ix,iy),(x,y),(0,0,0),3)
    elif event == cv2.EVENT_LBUTTONUP:
        if drawing:
            if mode:
                cv2.rectangle(img,(ix,iy),(x,y),(0,0,0),3)
            else:
                rad=int(np.sqrt((x-ix)**2+(y-iy)**2))
                cv2.circle(img,(ix,iy),rad,(0,0,0),3)
            drawing=False

img=np.ones((512,512,3),np.uint8)*255
cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint",draw)
while 1:
    cv2.imshow("Paint",img)
    k=cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()
