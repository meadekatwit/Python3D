import pygame, sys, random, time
from engine3D import *
from pygame.locals import *

c1 = Camera((0,0,0),(math.radians(0),0,0), math.radians(90))

points = [Point2D(0,0), Point2D(0,0)]

for i in range(30):
    points.append(Point2D(random.randint(-1, 1) * 10,(random.randint(-1, 1) * 10)))

SCREENX = 400
SCREENY = 300

pygame.init()
window = pygame.display.set_mode((SCREENX, SCREENY))
pygame.display.set_caption('Hello World!')

gameState = 0
zoom = 5
while True:
    time.sleep(0.01)
    keys = pygame.key.get_pressed()
    points[0] = c1.create2DTriangle(5)[0]
    points[1] = c1.create2DTriangle(5)[1]

    
    if gameState == 0:
        window.fill((0,0,0))
        pygame.draw.circle(window, (255, 255, 255),(SCREENX / 2.0 + c1.x * zoom, SCREENY / 2.0 - c1.y * zoom), 2)
        random.seed(0)
        for point in points:
            x = c1.portion2D(point)
            pygame.draw.circle(window, (random.randint(1,255), random.randint(1,255), random.randint(1,255)),(SCREENX / 2.0 + point.x * zoom, SCREENY / 2.0 - point.y * zoom), 2);
        

    elif gameState == 1:
        window.fill((0,0,0))
        random.seed(0)
        for point in points:
            x = c1.portion2D(point)
            pygame.draw.line(window, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), (SCREENX*x,0), (SCREENX*x, SCREENY), width=5);

    if keys[K_DOWN]: 
        c1.y -= 0.1
    if keys[K_UP]: 
        c1.y += 0.1
    if keys[K_LEFT]: 
        c1.x -= 0.1
    if keys[K_RIGHT]: 
        c1.x += 0.1

    if keys[K_q]: 
        c1.rx += 0.03
    if keys[K_e]: 
        c1.rx -= 0.03
    if keys[K_w]: 
        c1.x += math.cos(c1.rx) * 0.1
        c1.y += math.sin(c1.rx) * 0.1
    if keys[K_s]: 
        c1.x -= math.cos(c1.rx) * 0.1
        c1.y -= math.sin(c1.rx) * 0.1
    if keys[K_a]: 
        c1.x -= math.cos(c1.rx - math.pi / 2) * 0.1
        c1.y -= math.sin(c1.rx - math.pi / 2) * 0.1
    if keys[K_d]: 
        c1.x -= math.cos(c1.rx + math.pi / 2) * 0.1
        c1.y -= math.sin(c1.rx + math.pi / 2) * 0.1
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_1:
                gameState = 1
            if event.key == K_0:
                gameState = 0
            if event.key == K_v:
                for point in points:
                    x = c1.portion2D(point)
                    if (points.index(point) > 1):
                        print(points.index(point))
                        print(x)
    pygame.display.update()
