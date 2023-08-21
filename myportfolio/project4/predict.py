#import cv2 
#from ultralytics import YOLO
#from PIL import Image
#from pathlib import Path
#import time
#from django.templatetags.static import static
#import pickle
#import os
#model_path = os.path.join(os.path.dirname(__file__), 'best.pt')
from django.core.files import File
import torch

#model = YOLO(static('Project4/best.pt'))  
#dir_path = Path('/QR-codes')


#def deleteQR():
#    try:
#        dir_path.rmdir()
#    except OSError as e:
#        print("Error: %s : %s" % (dir_path, e.strerror))

def predict(p_image):

    model = torch.load("C:\Users\laco-\OneDrive\Documentos\GitHub\portfolio\myportfolio\project4\best.pt") 
#    deleteQR()
 #   source = p_image
 #   results = model.predict(source, conf =0.7)
 #   num_results = len(results[0].boxes.data)
 #   qcd = cv2.QRCodeDetector()
 #   for r in results:
 #           r.save_crop('')
 #   time.sleep(3)

    urls = ()
    imgs = ()
  #  for i in range(num_results):
  #      if i == 0:
  #          source = 'QR-codes/im.jpg'
            
  #      else:
   #         j =str(i+1)
   #         source = 'QR-codes/im'+j+'.jpg'
     
   #     img = cv2.imread(source)
   #     imgs.append(source)
  #      retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
 #       urls.append(decoded_info)
    
#    return{ 'hits': num_results, 'imgs': imgs, 'urls' : urls  }
    
    return{'imgs': imgs, 'urls' : urls  }