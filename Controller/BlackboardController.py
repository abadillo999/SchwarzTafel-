import cv2
import time
import sys



class BlackboardController:
    def __init__(self):
        print ("hello")
        self.image = cv2.imread('/media/sf_ShareCV/descarga.jpg', 0)

    def controll(self):
        print ("hello")

        cv2.imshow('hellouuu', self.image)
        time.sleep(10)
