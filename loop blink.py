import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
file=open('tim1.txt','r')
r=file.readline()
a=int(r[4])
while True:
    GPIO.output(8,True)
    time.sleep(a)
    GPIO.output(8,False)
    time.sleep(2)