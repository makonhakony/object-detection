# Object detection

## Prerequisite
Run setup script: [Vision Setup Bash Script](https://github.com/makonhakony/vision-setup-bash-script)
*note: this code runs well in RPI 4 and Bulleyes OS, I have not tested with other OS and system architecture*
### Required Installation
- Python 3 (>3.7)
- Tensorflow 2
- PIL
- Matplotlib
- Libcamera (if not Raspbian)
- picamera2
- tfhub

## Object Detection With Mobilenetv2

### Run with any input image
Run `python object_detection.py`

### Run with camera
Run `python object_detection_picamera.py`

## Object Detection With OpenCV2

### Run with any input image
Run `python object_detection_with_cv2.py`

### Run with camera
Run `python object_detection_picamera.py`
