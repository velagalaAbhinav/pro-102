import cv2 
def takeSnapShot():
    #starting the camera
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #reading the frames while camera is on 
        ret,frame = videoCaptureObject.read()
        #save image to any storage device
        cv2.imwrite('newpicture.jpg',frame)
        result = False
    #turning off the camera 
    videoCaptureObject.release()
    #closing all the windows that are open
    cv2.destroyAllWindows()
takeSnapShot()        