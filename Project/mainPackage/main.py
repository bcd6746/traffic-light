import cv2
import numpy
import matplotlib 
import os
import open3d as o3d

#How do we find the

def main(imgFiles, pointCloudfiles): 
    for filename in os.listdir(pointCloudfiles):
        # Check if the file is an image
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            print(imgFiles+"\\"+filename)
            vehicleInfo = findBoundingBox(cv2.imread(imgFiles+"\\"+filename))
        

def createVehicleInfo(file):
    imgeInfo = ImageInfo()
    fillVehics = fillVehics(file, ImageInfo)
    #call functions to set each element of the vehic class
   

def fillVehics(img,vehic):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    greyimg1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #create sift object
    sift = cv2.SIFT_create()  

    key_points, descriptors = sift.detectAndCompute(greyimg1, None)     

    keypointImage = cv2.drawKeypoints(img,key_points,None)   

    cv2.imshow("show",keypointImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows


  
if __name__=="__main__": 
    #LOAD Folders 
    imgFiles = "F:\\computer vision final project\\traffic-light\\dataset\\Images" 
    print(imgFiles)
    pointCloudFiles = "F:\\computer vision final project\\traffic-light\\dataset\PointClouds"
    main(imgFiles, pointCloudFiles)

class ImageInfo:
    def __init__(self):
        return
    def GetVelocity(self):
        return self.velocity
    def GetBoundingBox(self):
        return self.boundingbox
    def GetPosition(self):
        return self.position
    def GetBackground(self):
        return self.background
    def SetPosition(self,position):
        self.position = position
    def SetBoundingBox(self, boundingbox):
        self.boundingbox = boundingbox
    def SetVelocity(self, velocity):
        self.velocity = velocity
    def SetBackground(self, background):
        self.background = background
        