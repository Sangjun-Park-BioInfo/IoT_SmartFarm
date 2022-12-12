import picamera
import time

camera = picamera.PiCamera()

camera.resolution=(2560,1440)
camera.framerate=15
camera.brightness=55
camera.contrast=90
camera.start_preview()
time.sleep(15)
camera.capture("/home/psj/IoT/Project/Camera/image.jpg")
camera.stop_preview()


