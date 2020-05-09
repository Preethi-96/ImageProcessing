# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 23:51:45 2020

@author: User
"""
import numpy as np
from PIL import Image
import pandas as pd

import matplotlib.pyplot as plt
#import opencv as cv2
def FileConverterFxn(datFile, imgHt,imgWdt, strFrame, EndFrame, x1,y1,x2,y2):
  fp=open(datFile, 'r')
  #print(fp.dtypes)
  fp.seek(0)
  print(fp)
  print(fp.tell())
  matrix=np.zeros((y2-y1+1, x2-x1+1, EndFrame-strFrame+1))
  #print(matrix)
  frameSize = 48 + (imgHt*imgWdt*2)

  for fr in range(strFrame,EndFrame):
     
      offset = 2060 + 48 + (frameSize * fr)
      fp.seek(offset)
      #print(fp.tell())
      temp=np.zeros((imgHt,imgWdt))
      #print(temp)
      temp1=np.fromfile(fp,dtype='int16')
 
      temp=temp1[:imgHt*imgWdt].reshape((imgHt,imgWdt))
      temp=temp.transpose()

      for y in range(y1,y2):
          for x in range(x1,x2):
              matrix[y-y1+1,x-x1+1,fr-strFrame+1]=temp[y,x]
          


  r=matrix[:,:,48]
  plt.imshow(r,aspect='auto',interpolation='none',cmap='viridis', extent=[-0.5,31.5,63.5,-0.5] , origin='upper')
  plt.savefig('plot.png')
  print(r)
  #print(np.shape(r))
  #print(r)


  #plt.imshow(r,extent=[0,100,0,100],aspect='auto')

FileConverterFxn('data_20190731_01.dat',64,64,0,1000,33,1,64,64)            
      
  

