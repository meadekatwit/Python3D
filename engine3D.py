import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def angleBetween(self, p2):
        if (self.x == p2.x):
            if (self.y == p2.y):    #Directly on top
                return 0
            elif (self.y > p2.y):   #Directly Above
                return (math.pi / 2)
            else:                   #Directly Below
                return (3 * math.pi / 2)

        elif (self.x < p2.x):
            if (self.y < p2.y): #First Quadrant
                return math.atan((p2.y - self.y) / (p2.x - self.x))
            else:               #Fourth Quadrant
                return math.atan((p2.y - self.y) / (p2.x - self.x)) + 2 * math.pi
        else:
            if (self.y < p2.y): #Second Quadrant
                return math.atan((p2.y - self.y) / (p2.x - self.x)) + math.pi
            else:                #Third Quadrant
                return math.atan((p2.y - self.y) / (p2.x - self.x)) + math.pi

class Camera:
    def __init__(self, location, angle, fov):
        self.x = location[0]
        self.y = location[1]
        self.z = location[2]
        self.rx = angle[0]
        self.ry = angle[1]
        self.rz = angle[2]
        self.fov = fov

    def getOrigin2D(self):
        return Point2D(self.x, self.y)

    def portion2D(self, point):
        self.rx = self.rx % (2 * math.pi)
        
        angleToPoint = self.getOrigin2D().angleBetween(point)
        angleToEdge = (self.rx + (self.fov / 2))
        portion = ((angleToEdge - angleToPoint) / self.fov)

        if (portion < -3):
            angleToPoint = self.getOrigin2D().angleBetween(point) - 2 * math.pi
            portion = ((angleToEdge - angleToPoint) / self.fov)
        if (portion > 3):
            angleToPoint = self.getOrigin2D().angleBetween(point) + 2 * math.pi
            portion = ((angleToEdge - angleToPoint) / self.fov)
        
        return portion

    def create2DTriangle(self, drawDistance):
        return [ \
        Point2D((math.cos(self.rx + (self.fov / 2.0)) * drawDistance + self.x),   
              (math.sin(self.rx + (self.fov / 2.0)) * drawDistance + self.y)),  
        Point2D((math.cos(self.rx - (self.fov / 2.0)) * drawDistance + self.x),   
              (math.sin(self.rx - (self.fov / 2.0)) * drawDistance + self.y))]
        
c1 = Camera((10,0,0),(math.radians(0),0,0), math.radians(90))
p2 = Point2D(1,1)
p3 = Point2D(1,-1)
points = [p2, p3, p2, p3]
