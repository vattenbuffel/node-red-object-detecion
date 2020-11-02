# Intended to be used together with node-red.
# An image with the name "image_to_classify.jpg" should be uploaded via node-red to this folder.
# Then this script should be run which will classify the objects in the image and save a new image "image_classified.jpg".
# The image should then be uploaded to node-red and shown on the dashboard

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import tensorflow as tf
from yolov3.utils import detect_image, detect_realtime, detect_video, Load_Yolo_model, detect_video_realtime_mp
from yolov3.configs import *

image_path   = "image_to_classify.jpg"

#image_path   = "./IMAGES/kite.jpg"

yolo = Load_Yolo_model()
detect_image(yolo, image_path, "image_classified.jpg", input_size=YOLO_INPUT_SIZE, show=False, rectangle_colors=(255,0,0))

print("done classifying")