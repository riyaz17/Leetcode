import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
chan_list=[14,20]
chan_list2=[15,21]
GPIO.setup(chan_list,GPIO.OUT)
GPIO.setup(chan_list2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    if(GPIO.input(15)==False):
        GPIO.output(14,True)
        print("LED ON")
        time.sleep(1)
    else:
        GPIO.output(14,False)
        print("LED OFF")
        time.sleep(1)
    if(GPIO.input(21)==False):
        GPIO.output(20,True)
        print("LED ON")
        time.sleep(1)
    else:
        GPIO.output(20,False)
        print("LED OFF")
        time.sleep(1)