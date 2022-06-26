import cv2 as cv
import numpy as np

path = 'yor.jpg'
image = cv.imread(path,1)
flag = 1
user = int(input("Basic Operation in Opencv \n1. Displaying a Picture\n2. Access Pixel Value \n3. Modify Pixel Value \n4. Set Image Dimensions \n5. Set Image Total Pixel Count \n6. Check The Loaded Image Datatype\n"))
if user == 1:
    cv.imshow("Yor Forger", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if user == 2:
    inpx = int(input("Enter X coordinate: "))
    inpy = int(input("Enter Y coordinate: "))
    color = int(input("Choose a color channel: \n1. Blue \n2. Green\n3. Red \n"))
    if color == 3:
        color = 0
    print(image.item(inpx,inpy,color))

if user == 3:
    inpx = int(input("Enter X coordinate: "))
    inpy = int(input("Enter Y coordinate: "))
    inblue = int(input("Enter the value to change for Blue between 0-255: "))
    if inblue >255:
        print("Invalid Input!")
    ingreen = int(input("Enter the value to change for Green between 0-255: "))
    if ingreen >255:
        print("Invalid Input!")
    inred = int(input("Enter the value to change for Red between 0-255: "))
    if inred >255:
        print("Invalid Input!")
    print("Before: ", image[inpx,inpy])
    image.itemset((inpx,inpy,2),inred)
    image.itemset((inpx,inpy,1),ingreen)
    image.itemset((inpx,inpy,0),inblue)
    print("After: ", image[inpx,inpy])

if user == 4:
    shape = image.shape
    imgshape = (1000,1000,3)
    if imgshape[0] < shape[0] and imgshape[1] < shape[1]:
        print("The image loaded is not out of bounds!")
    else:
        print("The image loaded is out of bounds!")

if user == 5:
    size = image.size
    pxsize = 500000
    if size > pxsize:
        print("The set pixel count is lower than loaded image!")
    else:
        print("The set pixel count is higher than loaded image!")

if user == 6:
    print(image.dtype)







        
    
    














  



