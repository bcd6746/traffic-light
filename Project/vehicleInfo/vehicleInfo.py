class VehicleInfo:
    def __init__(self, velocity, boundingbox, position):
        self.velocity = velocity
        self.boundingbox = boundingbox
        self.position = position
    def GetVelocity(self):
        return self.velocity
    def GetBoundingBox(self):
        return self.boundingbox
    def GetPosition(self):
        return self.position
    def SetPosition(self,position):
        self.position = position
    def SetBoundingBox(self, boundingbox):
        self.boundingbox = boundingbox
    def SetVelocity(self, velocity):
        self.velocity = velocity