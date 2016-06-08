from picamera import PiCamera, Color
from time import sleep
import time
from datetime import datetime, timedelta
#import dateutil.tz
#from pytz import timezone
import os

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

dateString = '%H:%M:%S %d/%m/%Y %Z'
camera = PiCamera()
#camera.resolution = (2592, 1944)

#camera.framerate = 15

#camera.resolution = (64,64)
#camera.resolution = (128,128)
camera.resolution = (640, 480)
camera.annotate_text_size = 25

#camera.start_preview(alpha=200)
GPIO.setup(8, GPIO.OUT)


GPIO.output(8,GPIO.LOW)#turn led on and wait a few seconds
for i in range(2):
#    sleep(1800)
    GPIO.output(8, GPIO.HIGH)
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Plantography/camera/frame%s.jpg' %i)
    camera.annotate_text = (datetime.now()+ timedelta(hours = 1)).strftime(dateString);
    camera.capture('/home/pi/Plantography/camera/latest.jpg')
    camera.stop_preview()
    print ("capture completed")
    os.system("sudo cp /home/pi/Plantography/camera/latest.jpg /var/www/html/images")
    os.system("sudo cp /home/pi/Plantography/camera/frame%s.jpg /var/www/html/images"%i)
    print ("copy completed")
    GPIO.output(8,GPIO.LOW)
