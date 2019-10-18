from PIL import Image
import pytesseract
import os
import cv2
import pytesseract
import numpy as np
from PIL import Image
from io import BytesIO
import pandas as pd
import glob
import csv


#Let us assume all the pictures are stored in /home/user/Pictures/downloads
path = "/home/user/Pictures/downloads/*.*"
for file in glob.glob(path):
    a = cv2.imread(file)
    
indir = r'/home/user/Pictures/downloads/'
texts =[]
for root, dirs, filenames in os.walk(indir):
    for filename in filenames:
        im = Image.open(indir + filename)
        text = pytesseract.image_to_string(im, lang='eng')
        texts.append(text)
        df=pd.DataFrame(texts)
df.to_csv('/home/user/Pictures/downloads/output.csv', index=False)
#open the output file and see
