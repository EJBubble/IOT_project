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
### Finish to set up OpenCV environment

## Step 2: Set up the Pi Camera
### Installation

Install your Pi Camera on your Raspberry Pi  
🔗Link👉[Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/0)

### Test
Take a still picture and save it to the Desktop
```
raspistill -o Desktop/image.jpg
```
[IOT_3](https://github.com/EJBubble/IOT_project/blob/main/Pic/IOT_3.png)
### Finish to set up Pi Camera
