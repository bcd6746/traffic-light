import numpy as np
import os
import open3d as o3d
from matplotlib import pyplot as plt


#How do we find the

def main(imgFiles, pointCloudfiles): 
    for filename in os.listdir(pointCloudfiles):
        # Check if the file is an image
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            print(imgFiles+"\\"+filename)
            vehicleInfo = createVehicleInfo((imgFiles+"\\"+filename))

def FillVehics(img, ImageInfo):
    clusters = ClusterLidar(img)
    for clusts in clusters:
        if len(clusts)>10:
            print(clusts)


#create clusters to count and track the cars
#measure velocity from the movement of one frame to the next
#compare based on the closest cluster to the position of the cluster in the previous frame
def ClusterLidar(file):
    pcd = o3d.io.read_point_cloud(file)
    points = np.asarray(pcd.points)
    clustering = o3d.DBSCAN(eps=.5, min_samples=10).fit(points)
    cluster_labels = clustering.labels_
    visualize_clusters(points,cluster_labels)
    return cluster_labels

def createVehicleInfo(file):
    imgeInfo = ImageInfo()
    fillVehics = FillVehics(file, ImageInfo)

    #call functions to set each element of the vehic class

def visualize_clusters(points, cluster_labels):
    # Visualize clusters
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    unique_labels = set(cluster_labels)
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

    for cluster, color in zip(unique_labels, colors):
        cluster_points = points[cluster_labels == cluster]
        ax.scatter(cluster_points[:, 0], cluster_points[:, 1], cluster_points[:, 2], c=[color], marker='o', s=20)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


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
        