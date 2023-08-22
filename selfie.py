from picamera2 import Picamera2
from time import sleep

camera = Picamera2()

camera.start_preview()
sleep(5)
camera.capture_image('selfie.jpg')

camera.stop_preview()
