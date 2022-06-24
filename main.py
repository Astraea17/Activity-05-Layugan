import cv2 as cv
import numpy as np

#load immage
img = cv.imread("anya.jpg")

#check if image is rgb or grayscale image
if(len(img.shape)<2):
   print('\nImage type:Grayscale image')
   exit()
elif len(img.shape)==3:
   print('\nImage type:Colored image')

#image dimension and size limit
maxheight=720
maxwidth=1280
minheight=360
minwidth=480
size=1500000  

#set image dimensions and determine if it is within boundaries or not
print("\nImage dimension limit:max 1920x1080 and min 480x360")
imgheight=img.shape[0]
imgwidth=img.shape[1]
print("Current loaded image dimension:",imgheight,"x",imgwidth)
if((imgheight <= maxheight and imgheight >= minheight) and (imgwidth <= maxwidth and imgwidth >= minwidth)):
   print("Current loaded image is within the boundaries!")
else:
   print("Current loaded image is not in the boundaries!")

#show image data type
print("\nCurrent loaded image datatype:",img.dtype)

#Accessapixel value using item method
print("\nAccessapixel value using item method")
i,j,k = input("Enter row,column and channel:").split()
row1,column1,channel1=[int(i),int(j),int(k)]
res = img.item(row1,column1,channel1)
print("Result:",res)

#Modifyapixel value using itemset method
print("\nModify a pixel value using itemset method")
x,y = input("Enter row and column: ").split()
blue = int(input("Enter changes in blue channel: "))
green = int(input("Enter changes in green channel: "))
red = int(input("Enter changes in red channel: "))
print("\nResult")
row2,column2 = [int(x),int(y)]
img.item(row2,column2,0)
img.item(row2,column2,1)
img.item(row2,column2,2)
res1 = img[row2,column2]
print("Before:",res1)
img.itemset((row2,column2,0),blue)
img.itemset((row2,column2,1),green)
img.itemset((row2,column2,2),red)
res2=img[row2,column2]
print("After:",res2,"\n")