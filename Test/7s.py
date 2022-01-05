import RPi.GPIO as GPIO
import time
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
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
#routine to clear and then write to display
def digdisp(digit):
    for x in range (0,7):
        GPIO.output(gpin[x], digitclr[x])
    for x in range (0,7):
        GPIO.output(gpin[x], digit[x])
#routine to display digit from 0 to 9
digdisp(digitH)
time.sleep(1)
digdisp(digitE)
time.sleep(1)
digdisp(digitL)
time.sleep(1)
digdisp(digitn)
time.sleep(0.1)
digdisp(digitL)
time.sleep(1)
digdisp(digito1)
time.sleep(1)
digdisp(digitE)
time.sleep(1)
digdisp(digitR)
time.sleep(1)
digdisp(digitn)
time.sleep(0.1)
digdisp(digitR)
time.sleep(1)
digdisp(digito2)
time.sleep(1)
digdisp(digitR)
time.sleep(1)
#tidy up
GPIO.cleanup()
#import sys
#sys.exit()