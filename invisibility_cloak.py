import cv2
import time
import numpy as np

#To save the output in a file output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

#Starting the webcam
cap = cv2.VideoCapture(0)

#Allowing the webcam to start by making the code sleep for 2 seconds
time.sleep(2)
bg = 0

#Capturing background for 60 frames
for i in range(60):
    ret, bg = cap.read()
#Flipping the background
bg = np.flip(bg, axis=1)

#Reading the captured frame until the camera is open
while (cap.isOpened()):
   
    
    #Flipping the image for consistency
   

    #Converting the color from BGR to HSV
 

    #Generating mask to detect red colour(values can be changed)
    

    #Open and expand the image where there is mask 1 (color)
  

    #Selecting only the part that does not have mask one and saving in mask 2
   

    #Keeping only the part of the images without the red color 
    #(or any other color you may choose)
   

    #Keeping only the part of the images with the red color
   

    #Generating the final output by merging res_1 and res_2
    
    #Displaying the output to the user
    
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()
