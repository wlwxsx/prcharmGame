import pygame
#from pygame_function import *
# By Lisa and Jenny - all the images used are drawn by Lisa

pygame.init()

screen = pygame.display.set_mode((1440, 790))

left = False
right = False
up = False
down = False
running = True

clock = pygame.time.Clock()

# background
background = pygame.image.load("room.png")

#test
#testSprite = makeSprite("q.gif")

# title icon
pygame.display.set_caption("The Adventure of A Magic Cat")

# Player
PlayerI = pygame.image.load("o.png")

px = 200
py = 300
pxc = 0
pyc = 0
p1 = 0
p2 = 0
count = {"a": '0', "b": '0', "c": '0', "d": '0'}

# notif = pygame.image.load("n.png")
box1 = pygame.image.load("box.png")
box2 = pygame.image.load("box.png")
box3 = pygame.image.load("box.png")
box4 = pygame.image.load("box.png")
nt = False
nt1 = True
ma = True
ma1 = False
ma2 = False
t1 = False
t2 = False
t21 = True
t22 = False
t3 = False
t4 = False
fn = False
bg = False


walk = [pygame.image.load("o.png"), pygame.image.load("o.png"), pygame.image.load("o.png"),  pygame.image.load("o2.png"), pygame.image.load("o2.png"), pygame.image.load("o2.png"), pygame.image.load("o1.png"), pygame.image.load("o1.png"), pygame.image.load("o1.png")]
walkr = [pygame.transform.flip(pygame.image.load("o.png"), True, False), pygame.transform.flip(pygame.image.load("o.png"), True, False), pygame.transform.flip(pygame.image.load("o.png"), True, False), pygame.transform.flip(pygame.image.load("o1.png"), True, False), pygame.transform.flip(pygame.image.load("o1.png"), True, False), pygame.transform.flip(pygame.image.load("o1.png"), True, False), pygame.transform.flip(pygame.image.load("o2.png"), True, False), pygame.transform.flip(pygame.image.load("o2.png"), True, False), pygame.transform.flip(pygame.image.load("o2.png"), True, False)]


def f1(d, v):
    list = []

    for key in d:
        if str(d.get(key)) == v:
            return True
    if not list:
        return False
    return True


def player(x, y):
    screen.blit(PlayerI, (x, y))


def map1():
    global px
    global py
    global p1
    global p2

    global nt
    global nt1
    global background
    if px > 1300:
        px = p1
        py = p2
    if py < 130:
        px = p1
        py = p2
    if py > 670:
        px = p1
        py = p2
    if abs((400 - px)) < 100 and abs((350 - py)) < 100:
        nt = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            nt1 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                nt1 = False
    if px <= 200:
        if 200 < py < 400 and px < 100:
            background = pygame.image.load("l.png")
            px = -500
            py = -500
            redraw()
            pygame.time.delay(3000)
            background = pygame.image.load("map.png")
            px = 300
            py = 50
            pygame.display.update()
            global ma
            ma = False
            global ma1
            ma1 = True
        elif py <= 200 or py >= 400:
            px = p1
            py = p2
    print (px, py)


def map2():
    global px
    global py
    global p1
    global p2
    global background

    global t1
    global t2
    global t3
    global t4
    global t22
    global t21
    if 50 < px < 250 and py < 410:
        px = p1
        py = p2
    if 350 < px < 550 and py < 170:
        px = p1
        py = p2
    if 350 < px < 550 and py > 250:
        px = p1
        py = p2
    if 550 < px < 750 and 50 < py < 170:
        px = p1
        py = p2
    if 700 < px < 860 and 50 < py < 530:
        px = p1
        py = p2
    if 1000 < px < 1160 and 50 < py:
        px = p1
        py = p2
    if py > 670 or py < -10 or px < 0 or px > 1310:
        px = p1
        py = p2
    if px < 20 and py < 50:
        px = 20
        py = 55
        t1 = True
        t22 = True
        t21 = True
        pygame.display.update()
    if 350 > px > 300 and py > 575:
        px = 335
        py = 570
        t2 = True
        t22 = True
        t21 = True
        pygame.display.update()
    if 650 > px > 600 and py < 40:
        px = 680
        py = 40
        t3 = True
        t22 = True
        t21 = True
        pygame.display.update()
    if px > 1250 and py > 590:
        px = 1230
        py = 560
        t4 = True
        t22 = True
        t21 = True
        pygame.display.update()
    if not f1(count, '0'):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                global ma1
                # global fn
                global ma2
                background = pygame.image.load("food.png")
                t1 = False
                t2 = False
                t3 = False
                t4 = False
                fn = True
                ma2 = True
                ma1 = False

# print(px, py)


def map3():
    global background
    global px
    global py
    global bg
    global running
    px = -500
    py = -500

    if event.type == pygame.MOUSEBUTTONDOWN:
        background = pygame.image.load("food1.png")
        redraw()
        pygame.time.delay(3000)
        background = pygame.image.load("cake.png")
        redraw()
        pygame.time.delay(3000)
        background = pygame.image.load("cake1.png")
        redraw()
        pygame.time.delay(3000)
        bg = True
        redraw()
        pygame.time.delay(3000)
        running = False

# Loop
walkCount = 0



def redraw():
    # screen background color rgb
    # background image
    screen.blit(background, (0, 0))
    global nt
    global walkCount
    global p1
    global p2
    global count

    p1 = px
    p2 = py
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        screen.blit(walk[walkCount//3], (px, py))
        walkCount +=1
    elif right:
        screen.blit(walkr[walkCount // 3], (px, py))
        walkCount += 1
    elif up:
        screen.blit(walk[walkCount // 3], (px, py))
        walkCount += 1
    elif down:
        screen.blit(walk[walkCount // 3], (px, py))
        walkCount += 1
    else:
        player(px, py)
    if nt and nt1:
        screen.blit(pygame.image.load("start.png"), (450, 300))
        redraw()
        pygame.time.delay(3000)
        screen.blit(pygame.image.load("book.png"), (450, 300))
    if t1:
        screen.blit(box1, (17, 13))
        if t22 and t21:
            screen.blit(pygame.image.load("egg.png"), (450, 300))
            count["a"] = '1'

    if t2:
        screen.blit(box2, (390, 700))
        if t22 and t21:
            screen.blit(pygame.image.load("choc.png"), (450, 300))
            count["b"] = '1'

    if t3:
        screen.blit(box3, (603, 60))
        if t22 and t21:
            screen.blit(pygame.image.load("flour.png"), (450, 300))
            count["c"] = '1'

    if t4:
        screen.blit(box4, (1340, 710))
        if t22 and t21:
            screen.blit(pygame.image.load("milk.png"), (450, 300))
            count["d"] = '1'
    #if fn:
        #screen.blit(pygame.image.load("milk.png"), (450, 300))
    if bg:
        screen.blit(pygame.image.load("end.png"), (450, 300))
    pygame.display.update()


while running:
    clock.tick(27)
    # call to player and other objects
    px = px + pxc
    py = py + pyc

    # update screen
    pygame.display.update()

    # main character action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pxc -= 5
                left = True
                right = False
                up = False
                down = False
            elif event.key == pygame.K_RIGHT:
                pxc += 5
                left = False
                right = True
                up = False
                down = False
            elif event.key == pygame.K_UP:
                pyc -= 5
                left = False
                right = False
                up = True
                down = False
            elif event.key == pygame.K_DOWN:
                pyc += 5
                left = False
                right = False
                up = False
                down = True
            else:
                left = False
                right = False
                up = False
                down = False
                walkCount = 0
        if event.type == pygame.KEYUP:
            pxc = 0
            pyc = 0
            left = False
            right = False
            up = False
            down = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                t21 = False
                fn = False
                nt = False
                nt1 = False
    if ma:
        map1()
    if ma1:
        map2()
    if ma2:
        map3()
    redraw()
