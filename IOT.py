from flask import Flask, render_template, request, redirect, url_for, make_response
import time
import RPi.GPIO as GPIO
from datetime import timedelta

relay = 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT) # GPIO Assign mode
GPIO.output(relay, GPIO.LOW)

app = Flask(__name__) #set up flask server
#when the root IP is selected, return index.html page
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')    


#Uses methods from motors.py to send commands to the GPIO to operate the motors
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