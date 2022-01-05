import time
import RPi.GPIO as GPIO
 
BUTTON_PIN = 14
LED_PIN = 15
 
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)
 
try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            if GPIO.input(LED_PIN) == 0:
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.01)
                continue
            if GPIO.input(LED_PIN) == 1:
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(0.01)
                continue
    
except KeyboardInterrupt:
    print('關閉程式')
finally:
    GPIO.cleanup()