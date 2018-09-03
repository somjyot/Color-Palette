import cv2
import numpy as np

def empty():
    pass

def main():
    img=np.zeros((512,512,3),np.uint8)
    windowName='Color_palete'
    cv2.namedWindow(windowName)
    
    
    cv2.createTrackbar('B',windowName,0,255,empty)
    cv2.createTrackbar('G',windowName,0,255,empty)
    cv2.createTrackbar('R',windowName,0,255,empty)
    
    
    while(True):
        cv2.imshow(windowName,img)
        
        if cv2.waitKey(1) == 27 :
            break
        b=cv2.getTrackbarPos('B',windowName)
        g=cv2.getTrackbarPos('G',windowName)
        r=cv2.getTrackbarPos('R',windowName)
        
        img[:]=[b,g,r]
        
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()

