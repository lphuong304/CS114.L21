import os
import cv2
import random
import numpy as np
import tensorflow as tf
import pytesseract
from core.utils import read_class_names
from core.config import cfg
import pandas as pd
# function to count objects, can return total classes or count per class
roi_position = [0]
def get_price(key):
    if key == 'Pepsi Lon':
        return 9000
    elif key == 'Sua dac Phuong Nam':
        return 18500
def count_objects(id, data, by_class = True, allowed_classes = list(read_class_names(cfg.YOLO.CLASSES).values())):
    boxes, scores, classes, num_objects = data
    
    #example.setdefault('a', []).append('apple')
    # print('classes: ',classes, '\n') #một mảng gồm số pt bằng số class, giá trị pt thay đổi bởi số class đã được đánh
    # print("num_objects:", num_objects, '\n')
    #create dictionary to hold count of objects
    counts = dict()
    # if by_class = True then count objects per class
    if by_class:
        class_names = read_class_names(cfg.YOLO.CLASSES)
        #print(class_names) # dictionnary gồm các class với key là số 0,1,2,...số class - 1
        # loop through total number of objects found
        for i in range(num_objects):
            # grab class index and convert into corresponding class name
            class_index = int(classes[i]) #ép kiểu float sang int
            print('class_index: ', class_index,'\n')
            class_name = class_names[class_index] #gán key bằng với value tring class_names
            if class_name in allowed_classes:
                #counts[class_name] = list()
                counts[class_name] = counts.get(class_name, 0) + 1 #trả về giá trị ptu của key, nếu khong tìm đc giá trị trả về 0
                

                #get_price(str(class_name), counts)
            else:
                continue

    # else count total objects found
    else:
        counts['total object'] = num_objects
    #print(counts)
    return counts

# function for cropping each detection and saving as new image
def crop_objects(img, data, path, allowed_classes):
    boxes, scores, classes, num_objects = data
    class_names = read_class_names(cfg.YOLO.CLASSES)
    #create dictionary to hold count of objects for image name
    counts = dict()
    for i in range(num_objects):
        # get count of class for part of image name
        class_index = int(classes[i])
        class_name = class_names[class_index]
        if class_name in allowed_classes:
            counts[class_name] = counts.get(class_name, 0) + 1
            # get box coords
            xmin, ymin, xmax, ymax = boxes[i]
            # crop detection from image (take an additional 5 pixels around all edges)
            cropped_img = img[int(ymin)-5:int(ymax)+5, int(xmin)-5:int(xmax)+5]
            # construct image name and join it to path for saving crop properly
            img_name = class_name + '_' + str(counts[class_name]) + '.png'
            img_path = os.path.join(path, img_name )
            # save image
            cv2.imwrite(img_path, cropped_img)
        else:
            continue
        
# function to run general Tesseract OCR on any detections 
def ocr(img, data):
    boxes, scores, classes, num_objects = data
    class_names = read_class_names(cfg.YOLO.CLASSES)
    for i in range(num_objects):
        # get class name for detection
        class_index = int(classes[i])
        class_name = class_names[class_index]
        # separate coordinates from box
        xmin, ymin, xmax, ymax = boxes[i]
        # get the subimage that makes up the bounded region and take an additional 5 pixels on each side
        box = img[int(ymin)-5:int(ymax)+5, int(xmin)-5:int(xmax)+5]
        # grayscale region within bounding box
        gray = cv2.cvtColor(box, cv2.COLOR_RGB2GRAY)
        # threshold the image using Otsus method to preprocess for tesseract
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # perform a median blur to smooth image slightly
        blur = cv2.medianBlur(thresh, 3)
        # resize image to double the original size as tesseract does better with certain text size
        blur = cv2.resize(blur, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
        # run tesseract and convert image text to string
        try:
            text = pytesseract.image_to_string(blur, config='--psm 11 --oem 3')
            print("Class: {}, Text Extracted: {}".format(class_name, text))
        except: 
            text = None