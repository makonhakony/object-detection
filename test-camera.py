from picamera2.encoders import H264Encoder
from picamera2 import Picamera2,Preview
import time

camera = Picamera2()
camera_config = camera.create_preview_configuration()
camera.configure(camera_config)
camera.start_preview(Preview.QTGL, x=100, y=200, width=800, height=600)
camera.start()
#encoder = H264Encoder(bitrate=10000000)
#output="test.h264"

#camera.start_recording(encoder,output)

time.sleep(10)
#camera.stop_recording()
#camera.start_and_record_video("test.mp4", duration=5)

camera.stop_preview()
