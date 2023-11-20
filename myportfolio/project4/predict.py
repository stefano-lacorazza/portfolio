import cv2 
from ultralytics import YOLO
#from ultralytics.yolo.v8.detect.predict import DetectionPredictor
from PIL import Image
#from pathlib import Path
#import time
#from django.templatetags.static import static
#import pickle
#import os
#model_path = os.path.join(os.path.dirname(__file__), 'best.pt')
#import numpy as np
from django.core.files import File
import torch
from roboflow import Roboflow

#model = YOLO(static('Project4/best.pt'))  
#dir_path = Path('/QR-codes')


#def deleteQR():
#    try:
#        dir_path.rmdir()
#    except OSError as e:
#        print("Error: %s : %s" % (dir_path, e.strerror))

def predict(p_image):
    model = YOLO(r"C:\Users\laco-\OneDrive\Documentos\GitHub\portfolio\myportfolio\project4\best.pt")
    #model = YOLO(r"/home/laco89/portfolio/myportfolio/project4/best.pt")
    path = r'C:\Users\laco-\OneDrive\Documentos\GitHub\portfolio\myportfolio\media\images'+'\\'+p_image
    #path = r'/home/laco89/portfolio/myportfolio/media/images'+'/'+p_image
    #path = r'/home/laco89/C:/Users/laco-/OneDrive/Documentos/GitHub/portfolio/myportfolio/media/images'+'/'+p_image
    #results = model.predict(p_image, conf =0.5)
    results = model(path, conf =0.6)
    
    num_results = len(results[0].boxes.data)
    qcd = cv2.QRCodeDetector()
    for r in results:
        r.save_crop(r'C:\Users\laco-\OneDrive\Documentos\GitHub\portfolio\myportfolio\static')
        #r.save_crop(r'\home\laco89\portfolio\myportfolio\static')

    urls = []
    imgs = []
    for i in range(num_results):
        if i == 0:
            source = r'\static\QR-codes\im.jpg'
            
        else:
            j =str(i+1)
            source = r'\static\QR-codes\im'+j+'.jpg'
     
        img = cv2.imread("C:\\Users\\laco-\\OneDrive\\Documentos\\GitHub\\portfolio\\myportfolio"+'\\'+source)


        #img = cv2.imread("/home/laco89/portfolio/myportfolio/"+source)
        imgs.append(source)
        try:
            retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
            if retval:
                urls.append(decoded_info[0])
        except OSError as e:
            print("Error")
    
    return{ 'hits': num_results, 'imgs': imgs, 'urls' : urls  }
    
