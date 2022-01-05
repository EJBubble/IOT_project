import cv2
import numpy as np
import os
import time
import RPi.GPIO as GPIO
import pygame

k = 0

i = 0

BUTTON_PIN = 14
LED_PIN = 15
relay = 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(relay, GPIO.OUT) # GPIO Assign mode
GPIO.output(relay, GPIO.LOW)


#setup output pins
GPIO.setup(19, GPIO.OUT)      #GPIO19
GPIO.setup(18, GPIO.OUT)      #GPIO18
GPIO.setup(16, GPIO.OUT)      #GPIO16
GPIO.setup(13, GPIO.OUT)      #GPIO13
GPIO.setup(12, GPIO.OUT)      #GPIO12
GPIO.setup(20, GPIO.OUT)      #GPIO20
GPIO.setup(21, GPIO.OUT)      #GPIO21


#define 7 segment digits
digitclr=[1,1,1,1,1,1,1]
digitH=[0,1,1,0,1,1,1]
digitE=[1,0,0,1,1,1,1]
digitL=[0,0,0,1,1,1,0]
digito1=[1,1,1,1,1,1,0]
digito2=[0,0,1,1,1,0,1]
digitR=[0,0,0,0,1,0,1]
digitn=[0,0,0,0,0,0,0]
gpin=[19,18,16,13,12,20,21]

def digdisp(digit):
    for x in range (0,7):
        GPIO.output(gpin[x], digitclr[x])
    for x in range (0,7):
        GPIO.output(gpin[x], digit[x])

      
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/ej108403545/FaceDetection/trainer/trainer.yml')
cascadePath = "/home/ej108403545/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX
 
#iniciate id counter
id = 0
 
# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'EJ', 'PaulLiu', 'GoodGUY', 'Z', 'W'] 
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW: 
            if GPIO.input(LED_PIN) == 0:
                  
                    
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.01)
                time.sleep(0.01)
                
                while True:
                    
                    if i==1 and GPIO.input(relay) == GPIO.LOW:
                        cv2.destroyAllWindows()
                        i = 0
                        break
                    
                    
                    ret, img =cam.read()
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     
                    faces = faceCascade.detectMultiScale( 
                        gray,
                        scaleFactor = 1.2,
                        minNeighbors = 5,
                        minSize = (int(minW), int(minH)),
                       )
 
                    for(x,y,w,h) in faces:
                        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
 
                        # Check if confidence is less them 100 ==> "0" is perfect match 
                        if (confidence < 60):
                            id = names[id]
                            confidence = "  {0}%".format(round(100 - confidence))
                            
                            if(i == 0):
                                print("Hello")
                                
                                GPIO.output(relay, GPIO.HIGH)
                                
                                pygame.mixer.init()
                                pygame.mixer.music.load('hello.mp3')
                                pygame.mixer.music.play()
                                
                                digdisp(digitH)
                                time.sleep(0.8)
                                digdisp(digitE)
                                time.sleep(0.8)
                                digdisp(digitL)
                                time.sleep(0.8)
                                digdisp(digitn)
                                time.sleep(0.1)
                                digdisp(digitL)
                                time.sleep(0.8)
                                digdisp(digito1)
                                time.sleep(0.8)
                                
                                i+=1
                                
                                
                        
                        else:
                            id = "unknown"
                            confidence = "  {0}%".format(round(100 - confidence))
                            
                            if(i == 0):
                                print("Error")
                                
                                cv2.imwrite("/home/ej108403545/FaceDetection/static/error.jpg",img)
                                
                                pygame.mixer.init()
                                pygame.mixer.music.load('error.mp3')
                                pygame.mixer.music.play()
                                digdisp(digitE)
                                time.sleep(0.8)
                                digdisp(digitR)
                                time.sleep(0.8)
                                digdisp(digitn)
                                time.sleep(0.2)
                                digdisp(digitR)
                                time.sleep(0.8)
                                digdisp(digito2)
                                time.sleep(0.8)
                                digdisp(digitR)
                                time.sleep(0.8)
                                
                                i+=2
                                
                    
         
                        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
     
                    cv2.imshow('camera',img)
                    
                    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
                    if k == 27:
                        cv2.destroyAllWindows()
                        i = 0
                        break
            
            if GPIO.input(LED_PIN) == 1:
                
                GPIO.output(LED_PIN, GPIO.LOW)
                GPIO.output(relay, GPIO.LOW)
            
                time.sleep(0.01)
                

                
    
    
except KeyboardInterrupt:
    print('關閉程式')
finally:
    GPIO.cleanup()
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

