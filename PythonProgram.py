# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 23:51:45 2020

@author: User
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import opencv as cv2
from PIL import Image
def FileConverterFxn(datFile, imgHt,imgWdt, strFrame, EndFrame, x1,y1,x2,y2):
  fp=open(datFile, 'r')
  #print(fp.dtypes)
  fp.seek(0)
  matrix=np.zeros((y2-y1+1, x2-x1+1, EndFrame-strFrame+1))
  #print(matrix)
  frameSize = 48 + (imgHt*imgWdt*2)
  d=1
  for fr in range(strFrame,160):
     
      offset = 2060 + 48 + (frameSize * fr)
      fp.seek(offset)
      temp=np.zeros((imgHt,imgWdt))
      #print(temp)
      temp1=np.fromfile(fp,dtype='>i2')
      temp=temp1[:imgHt*imgWdt].reshape((imgHt,imgWdt))
      print(temp)
      print(temp.ndim)
      print(temp.shape)
     
      for y in range(y1,y2):
          for x in range(x1,x2):
              matrix[y-y1+1][x-x1+1][fr-strFrame+1]=temp[y][x]
              #matrix=Image.fromarray(temp[y:x],'L')
              #img.show()
              
              #print(temp(x,y))
             #matrix(( y-y1+1, x-x1+1, fr-strFrame+1)) = temp ((y, x ))
             
             #plt.imshow(temp(x,y))
             #plt.show()'''
     
      print(matrix)
      
      #plt.imshow(cv2.cvtColor(matrix, cv2.COLOR_BGR2RGB))
      
      #Img=Image.fromarray(np.uint8(matrix[..., fr-strFrame+1]),'L')
      Img=Image.fromarray((matrix[..., fr-strFrame+1]),'RGB')
      Img=Img.resize( [int(5 * s) for s in Img.size])
      filename = "%d.jpg"%d
      Img.save(filename)
      d+=1
FileConverterFxn('data_20190731_02.dat',64,64,150,2000,33,1,64,64)            
      
  

