import cv2
import numpy

def main(files): 
    for file in files:
        #call function to find bounding box of vehicle and pass back an object that contains the cloud
        #position, bounding box, and motion vector
        vehicleInfo = createVehicleInfo(files)


  
  
if __name__=="__main__": 
    #LOAD FILE 
    files=cv2.imread("filename for folder")
    main(files)