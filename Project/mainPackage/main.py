import cv2
import numpy
import VehicleInfo

def main(imgFiles, pointCloudfiles): 
    for file in pointCloudfiles:
        #call function to find bounding box of vehicle and pass back an object that contains the cloud
        #position, bounding box, and motion vector
        vehicleInfo = createVehicleInfo(file)
        

def createVehicleInfo(file):
    vehic = VehicleInfo()
    #call functions to set each element of the vehic class
    vehic.SetPosition((findPosition(file)))
    vehic.SetBoundingBox((findBoundingBox(file)))
    vehic.SetVelocity((findVelocity(file)))

def findBoundingBox(file):
    return

def findVelocity(file):
    return

def findPosition(file):
    return

  
  
if __name__=="__main__": 
    #LOAD Folders 
    files=cv2.imread("dataset\Images")
    files=cv2.imread("dataset\PointClouds")
    main(files)