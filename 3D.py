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

        self.origin2D = Point2D(self.x, self.y)

    def portion2D(self, point):
        angleToPoint = self.origin2D.angleBetween(point)
        angleToEdge = (self.rx + (self.fov / 2))
        return ((angleToEdge - angleToPoint) / self.fov)

    def create2DTriangle(self, drawDistance):
        return [ \
        Point2D((math.cos(self.rx + (self.fov / 2.0)) * drawDistance + self.x),   
              (math.sin(self.rx + (self.fov / 2.0)) * drawDistance + self.y)),  
        Point2D((math.cos(self.rx - (self.fov / 2.0)) * drawDistance + self.x),   
              (math.sin(self.rx - (self.fov / 2.0)) * drawDistance + self.y))]
        

c1 = Camera((0,0,0),(math.radians(45),0,0), math.radians(90))
print(c1.create2DTriangle(20)[0])
p2 = Point2D(5,5)
print(c1.portion2D(p2))
