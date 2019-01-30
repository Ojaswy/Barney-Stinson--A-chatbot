import time
import cv2
from PIL import Image

camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(0.1)  #Time for capture, else image will be dark
return_value, image = camera.read()
cv2.imwrite("click.png", image)
img = Image.open('click.png')
img.show()
del(camera)  

