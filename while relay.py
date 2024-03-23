import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.output(8,True)
while True:
    GPIO.output(32,True)
    time.sleep(1)
    GPIO.output(32,False)
    time.sleep(1)