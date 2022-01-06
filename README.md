# IOT FINAL PROJECT -- *IOT SAFE*

---
![IOT_2](https://github.com/EJBubble/IOT_project/blob/main/Pic/IOT_2.jpg)
___

## Overview
**_IOT SAFE_** is an IOT project that can help you who need to protect your personal privacy. You can go anywhere at ease after you lock the safe. Therefore, you can place the IOT SAFE in your room or your dormitory to avoid someone from stealing your important things.


## Background
Someone like to eat my snack actively  :cry:

## Features
1. Use the face detection to control the lock mainly
2. Play sound to check whether the face detection is successful
3. Output the hint that you can know if the face detection is successful by seven segement
4. Open or close the lock by website
5. Get the intruder's photo and upload to the website

## Components
### Hardware
- NoteBook *1
- Raspberry Pi 4 *1
- Jumper wires 
- 12V Switching Power Supply *1
- 4 Channel DC 5V Relay Module *1
- Breadboard *1
- 3.5mm Speaker *1
- Pi Camera *1
- Solenoid Lock 12V *1
- One Digit Seven Segement *1
- LED *1
- [Push Button](https://www.amazon.com/-/zh_TW/Taiss-100-PCB-%E7%9E%AC%E6%99%82%E8%A7%B8%E8%A6%BA%E6%8C%89%E9%88%95%E9%96%8B%E9%97%9C-DIP/dp/B0796QHL5Z/ref=sr_1_5?keywords=raspberry+pi+buttons&qid=1641445335&sr=8-5) *1
---
### Safe
- PP sheet *6
- Glue Gun *1
- [Door shaft](https://shopee.tw/%F0%9F%92%97%E6%9A%96%E6%9A%96%E5%AE%B6%E5%B1%85%F0%9F%92%974%E5%AF%B8304%E4%B8%8D%E9%8A%B9%E9%8B%BC%E5%90%88%E9%A0%81%E9%96%80%E5%90%88%E8%91%89%E5%B9%B3%E9%96%8B%E6%9C%A8%E9%96%80%E5%8A%A0%E5%8E%9A%E9%9D%9C%E9%9F%B3%E8%BB%B8%E6%89%BF%E9%96%80%E6%8A%98%E9%A0%81%E6%B4%BB%E9%A0%81%E6%88%BF%E9%96%80%E6%8A%98%E5%8F%A0-i.511099052.10350192261?sp_atk=4ec3e282-be2e-4bbb-89c4-42b0a98595ea) *2
- Double-sided tape *1
- Utility knife *1
---
### Enviornment
- Rapsberry OS
- OpenCV 3.2.0
- Python 3.7

## Step 1: Set up the OpenCV Environment
### Introduction
OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products.The library has more than 2500 optimized algorithms, which includes a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms.These algorithms can be used to detect and recognize faces, identify objects, etc.

### Installation
- Update software
```
sudo apt-get update
sudo apt-get upgrate
```
---
- Install software that OpenCV can compile
```
sudo apt-get install cmake build-essential pkg-config git
```
---
- Install support software
```
//image
sudo apt-get install libjpeg-dev libtiff-dev libjasper-dev libpng-dev libwebp-dev libopenexr-dev
//video
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libdc1394–22-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
```
---
- Install tools
```
//Software that Opencv need
sudo apt-get install libgtk-3-dev libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
sudo apt-get install libatlas-base-dev liblapacke-dev gfortran
//HDF5
sudo apt-get install libhdf5-dev libhdf5–103
//Python
sudo apt-get install python3-dev python3-pip python3-numpy
```
---
- Modify swapfile  

Raspberry Pi will need enough swap to install OpenCV.
```
sudo nano /etc/dphys-swapfile
```
Find this code `CONF_SWAPSIZE=100`.  
Change to `CONF_SWAPSIZE=2048`.  
Press `CTRL+O`, and then press `ENTER` to save the file.  
Press `CTRL+X` to leave.  
Then, reboot swapfile.  
```
sudo systemctl restart dphys-swapfile
```
___
- Get OpenCV and OpenCV-contrib
```
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
```
---
- Create directory and Change it
```
mkdir ~/opencv/build
cd ~/opencv/build
```
---
- Init the configuration and Cmake 
```
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules -D ENABLE_NEON=ON -D ENABLE_VFPV3=ON -D BUILD_TESTS=OFF -D INSTALL_PYTHON_EXAMPLES=OFF -D OPENCV_ENABLE_NONFREE=ON -D CMAKE_SHARED_LINKER_FLAGS=-latomic -D BUILD_EXAMPLES=OFF ..
```
- Let Raspberry Pi kernel allow to compile OpenCV 
```
make -j$(nproc)
```
---
- Intall OpenCV
```
sudo make install
sudo ldconfig
```
---
- Modify swapfile  

After the installation of OpenCV, Raspberry Pi don't need swap.
```
sudo nano /etc/dphys-swapfile
```
Find this code `CONF_SWAPSIZE=2048`.  
Change to `CONF_SWAPSIZE=100`.  
Press `CTRL+O`, and then press `ENTER` to save the file.  
Press `CTRL+X` to leave.  
Finally, reboot swapfile.
```
sudo systemctl restart dphys-swapfile
```
---
- Install OpenCV and OpenCV-contrib for python
```
sudo pip3 install opencv-python
sudo pip3 pip install opencv-contrib-python
```
### *__Finish to set up OpenCV environment__*

## Step 2: Set up the Pi Camera
### Installation

Install your Pi Camera on your Raspberry Pi  
🔗Link👉[Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/0)

### Test
Take a still picture and save it to the Desktop
```
raspistill -o Desktop/image.jpg
```
![IOT_3](https://github.com/EJBubble/IOT_project/blob/main/Pic/IOT_3.png)  
### *__Finish to set up Pi Camera__*

## Step 3: Install seven segement、push button、relay module、power supply and 3.5mm speaker
![IOT_5](https://github.com/EJBubble/IOT_project/blob/main/Pic/IOT_5.jpg)

### Circuit diagram
![IOT_bb](https://github.com/EJBubble/IOT_project/blob/main/Pic/IOT_bb.png)

### 3.5mm speaker
![IOT_4](https://github.com/EJBubble/IOT_project/blob/main/Pic/IOT_4.jpg)
### *__Finish to install seven segement、push button、relay module、power supply and 3.5mm speaker__*

## Step 3.1: Make the Safe
![IOT_6](https://github.com/EJBubble/IOT_project/blob/main/Pic/IOT_6.jpg)
![IOT_7](https://github.com/EJBubble/IOT_project/blob/main/Pic/IOT_7.jpg)

## Step 4: Install Python library that the project need
```
//RPi.GPIO
sudo apt-get install python3-rpi.gpio
//numpy
sudo pip3 install numpy
//pygame
//It can play sound by executing python
sudo pip3 install pygame
//datetime
sudo pip3 install datetime
//Flask
sudo pip3 install Flask
//pillow
sudo pip3 install pillow
```
## Step 5 : Clone the file from github
```
git clone https://github.com/EJBubble/IOT_project.git
```

## Step 6 : Get Face Sample
Take the Pi camera and execute `Cap.py`
```
cd IOT_project
sudo python3 Cap.py
```
```python
#Cap.py
import cv2
import os
 
#捕獲圖像
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

#引入預訓練分類器
#User: your username
face_detector = cv2.CascadeClassifier('/home/User/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
 
# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
 
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
 
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #gray 表示轉換 grayscale 圖像 (人臉辨識在grayscale 圖像下進行)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    #x,y,w,h得到人臉數據
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
 
        # Save the captured image into the datasets folder
        # User: your username
        cv2.imwrite("/home/User/IOT_project/dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        
        #顯示
        cv2.imshow('image', img)
 
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break
 
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
```
### Your samples will be stored in the file `dataset`

## Step 7: Train the recognizer
Execute `train.py`
```
sudo python3 train.py
```
```python
#train.py
import numpy as np
from PIL import Image
import os
import cv2
 
# Path for face image database
# User: your username
path = '/home/User/IOT_project/dataset'
#LBPHFaceRecognizer人臉識别器由OpenCV提供
recognizer = cv2.face.LBPHFaceRecognizer_create()
# User: your username
detector = cv2.CascadeClassifier("/home/User/opencv/data/haarcascades/haarcascade_frontalface_default.xml");
 
# function to get the images and label data
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids
 
print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
 
# Save the model into trainer/trainer.yml
recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
 
# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
```
### trainer.yml will be stored in the file 'trainer'

## Step 8: Finish the Safe
Open two terminals  
- Execute `IOT.py` on one terminal
```
sudo python3 IOT.py
```

```python
#IOT.py
from flask import Flask, render_template, request, redirect, url_for, make_response
import time
import RPi.GPIO as GPIO
from datetime import timedelta

#Pin of relay module
relay = 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT) # GPIO Assign mode
GPIO.output(relay, GPIO.LOW)

app = Flask(__name__) #set up flask server
#when the root IP is selected, return index.html page
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#telling the Flask that what URL should trigger our function
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')    


#Uses methods from motors.py to send commands to the GPIO to control the solenoid lock
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin) #cast changepin to an int
    if changePin == 1:
        print("ON")
        GPIO.output(relay, GPIO.HIGH)
    elif changePin == 2:
        print("OFF")
        GPIO.output(relay, GPIO.LOW)
    response = make_response(redirect(url_for('index')))
    return(response)

  
app.run(debug=True, host='0.0.0.0', port='80')
```
![IOT_1](https://github.com/EJBubble/IOT_project/blob/main/Pic/IOT_1.png)
- Execute `all.py` on another terminal
```
sudo python3 all.py
```

```python
#all.py
import cv2
import numpy as np
import os
import time
import RPi.GPIO as GPIO
import pygame

#init cv2.waitKey
k = 0

i = 0

#set PIN
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

#output 7 segment
def digdisp(digit):
    for x in range (0,7):
        GPIO.output(gpin[x], digitclr[x])
    for x in range (0,7):
        GPIO.output(gpin[x], digit[x])

#Recognize      
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/user/IOT_project/trainer/trainer.yml')
cascadePath = "/home/User/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
#User: your username

font = cv2.FONT_HERSHEY_SIMPLEX
 
#iniciate id counter
id = 0
 
# names related to ids: example ==> GoodGuy: id=1,  etc
names = ['None', 'GoodGuy', 'GoodGuy', 'GoodGuy', 'GoodGuy', 'GoodGuy'] 
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
        if GPIO.input(BUTTON_PIN) == GPIO.LOW: #Detect Button
            if GPIO.input(LED_PIN) == 0:  #Detect LED
                  
                #Open LED    
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.01)
                time.sleep(0.01)
                
                while True:
                    #Detect the control lock whether to lock
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
 
                        # Check confidence of detect face
                        if (confidence < 60):
                            id = names[id]
                            confidence = "  {0}%".format(round(100 - confidence))
                            
                            if(i == 0):
                                print("Hello")
                                #open the lock
                                GPIO.output(relay, GPIO.HIGH)
                                #play hellosound
                                pygame.mixer.init()
                                pygame.mixer.music.load('hello.mp3')
                                pygame.mixer.music.play()
                                #output 7 segment
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
                                
                                #output only one times
                                i+=1
                                
                                
                        
                        else:
                            id = "unknown"
                            confidence = "  {0}%".format(round(100 - confidence))
                            
                            if(i == 0):
                                print("Error")
                                #detect the bad guy and take a picture 
                                cv2.imwrite("/home/ej108403545/FaceDetection/static/error.jpg",img)
                                #play error sound
                                pygame.mixer.init()
                                pygame.mixer.music.load('error.mp3')
                                pygame.mixer.music.play()
                                #output 7 segment
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
                                
                                #output only one times
                                i+=2
                                
                    
         
                        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
     
                    cv2.imshow('camera',img)
                    
                    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
                    if k == 27:
                        cv2.destroyAllWindows()
                        i = 0
                        break
            #detect Led
            if GPIO.input(LED_PIN) == 1:
                #Close the lock
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
 ```

