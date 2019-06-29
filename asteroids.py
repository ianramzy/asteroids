import pygame, sys, random
import math

pygame.init()
pygame.key.set_repeat(10)
size = width, height = 1680, 1050
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption('Roidz')

backround = pygame.image.load("res/roidz1.gif")
backrect = backround.get_rect()
backround2 = pygame.image.load("res/roidz2.gif")
backrect = backround2.get_rect()
backround3 = pygame.image.load("res/roidz3.gif")
backrect = backround3.get_rect()
backround4 = pygame.image.load("res/roidz4.gif")
backrect = backround4.get_rect()
backround5 = pygame.image.load("res/roidz5.gif")
backrect = backround5.get_rect()
backround6 = pygame.image.load("res/roidz6.gif")
backrect = backround6.get_rect()
backround7 = pygame.image.load("res/roidz7.gif")
backrect = backround7.get_rect()
backround8 = pygame.image.load("res/roidz8.gif")
backrect = backround8.get_rect()
backround9 = pygame.image.load("res/roidz9.gif")
backrect = backround9.get_rect()
backround10 = pygame.image.load("res/roidz10.gif")
backrect = backround10.get_rect()
backround11 = pygame.image.load("res/roidz11.gif")
backrect = backround11.get_rect()
backround12 = pygame.image.load("res/roidz12.gif")
backrect = backround12.get_rect()
backround13 = pygame.image.load("res/roidz13.gif")
backrect = backround13.get_rect()
backround14 = pygame.image.load("res/roidz14.gif")
backrect = backround14.get_rect()


def lose():
    font1 = pygame.font.Font("res/pixelmix_bold.ttf", 88)
    font2 = pygame.font.Font("res/pixelmix_bold.ttf", 222)
    backcount = 0
    teal = [0, 150, 255]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_RETURN]:
                game()

        backcount = backcount + 1
        if backcount == 1:
            screen.blit(backround, backrect)
        if backcount == 2:
            screen.blit(backround2, backrect)
        if backcount == 3:
            screen.blit(backround3, backrect)
        if backcount == 4:
            screen.blit(backround4, backrect)
        if backcount == 5:
            screen.blit(backround5, backrect)
        if backcount == 6:
            screen.blit(backround6, backrect)
        if backcount == 7:
            screen.blit(backround7, backrect)
        if backcount == 8:
            screen.blit(backround8, backrect)
        if backcount == 9:
            screen.blit(backround9, backrect)
        if backcount == 10:
            screen.blit(backround10, backrect)
        if backcount == 11:
            screen.blit(backround11, backrect)
        if backcount == 12:
            screen.blit(backround12, backrect)
        if backcount == 13:
            screen.blit(backround13, backrect)
        if backcount == 14:
            screen.blit(backround14, backrect)
            backcount = 0

        renderedText = font1.render("Press Enter to Play Again", 1, teal)
        screen.blit(renderedText, (22, height - 195))
        renderedText = font2.render("YOU LOSE", 1, teal)
        screen.blit(renderedText, (178, 95))

        pygame.display.flip()
        # pygame.time.wait(10)


def lose():
    font1 = pygame.font.Font("res/pixelmix_bold.ttf", 88)
    font2 = pygame.font.Font("res/pixelmix_bold.ttf", 222)
    backcount = 0
    teal = [0, 150, 255]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_RETURN]:
                game()

        backcount = backcount + 1
        if backcount == 1:
            screen.blit(backround, backrect)
        if backcount == 2:
            screen.blit(backround2, backrect)
        if backcount == 3:
            screen.blit(backround3, backrect)
        if backcount == 4:
            screen.blit(backround4, backrect)
        if backcount == 5:
            screen.blit(backround5, backrect)
        if backcount == 6:
            screen.blit(backround6, backrect)
        if backcount == 7:
            screen.blit(backround7, backrect)
        if backcount == 8:
            screen.blit(backround8, backrect)
        if backcount == 9:
            screen.blit(backround9, backrect)
        if backcount == 10:
            screen.blit(backround10, backrect)
        if backcount == 11:
            screen.blit(backround11, backrect)
        if backcount == 12:
            screen.blit(backround12, backrect)
        if backcount == 13:
            screen.blit(backround13, backrect)
        if backcount == 14:
            screen.blit(backround14, backrect)
            backcount = 0

        renderedText = font1.render("Press Enter to Play Again", 1, teal)
        screen.blit(renderedText, (22, height - 195))
        renderedText = font2.render("YOU LOSE", 1, teal)
        screen.blit(renderedText, (178, 95))

        pygame.display.flip()
        # pygame.time.wait(10)


def start():
    import pygame, sys, random
    import math
    pygame.init()
    pygame.key.set_repeat(10)
    size = width, height = 1680, 1050
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption('Roidz')

    # pygame.mixer.music.load('roidstartmusic.wav')
    # pygame.mixer.music.play(-1)

    font1 = pygame.font.Font("res/pixelmix_bold.ttf", 111)
    font2 = pygame.font.Font("res/pixelmix_bold.ttf", 222)
    font3 = pygame.font.Font("res/pixelmix_bold.ttf", 22)

    backcount = 1
    teal = [0, 150, 255]
    black = [0, 0, 0]
    white = [255, 255, 255]
    green = [0, 255, 0]
    red = [255, 0, 0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_SPACE]:
                game()
            if keys[pygame.K_i]:
                inst()

        backcount = backcount + 1
        if backcount == 1:
            screen.blit(backround, backrect)
        if backcount == 2:
            screen.blit(backround2, backrect)
        if backcount == 3:
            screen.blit(backround3, backrect)
        if backcount == 4:
            screen.blit(backround4, backrect)
        if backcount == 5:
            screen.blit(backround5, backrect)
        if backcount == 6:
            screen.blit(backround6, backrect)
        if backcount == 7:
            screen.blit(backround7, backrect)
        if backcount == 8:
            screen.blit(backround8, backrect)
        if backcount == 9:
            screen.blit(backround9, backrect)
        if backcount == 10:
            screen.blit(backround10, backrect)
        if backcount == 11:
            screen.blit(backround11, backrect)
        if backcount == 12:
            screen.blit(backround12, backrect)
        if backcount == 13:
            screen.blit(backround13, backrect)
        if backcount == 14:
            screen.blit(backround14, backrect)
            backcount = 0

        renderedText = font1.render("Press Space to Play", 1, teal)
        screen.blit(renderedText, (55, height - 195))
        renderedText = font3.render("'i'", 1, teal)
        screen.blit(renderedText, (1655, 6))

        renderedText = font2.render("Asteroids", 1, teal)
        screen.blit(renderedText, (78, 95))

        pygame.display.flip()
        # pygame.time.wait(10)


def inst():
    import pygame, sys, random
    import math
    pygame.init()
    pygame.key.set_repeat(10)
    size = width, height = 1680, 1050
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption('Roidz')
    font1 = pygame.font.Font("res/pixelmix_bold.ttf", 51)
    font2 = pygame.font.Font("res/pixelmix_bold.ttf", 172)
    backcount = 1
    teal = [0, 150, 255]
    black = [0, 0, 0]
    white = [255, 255, 255]
    green = [0, 255, 0]
    red = [255, 0, 0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_SPACE]:
                game()

        backcount = backcount + 1
        if backcount == 1:
            screen.blit(backround, backrect)
        if backcount == 2:
            screen.blit(backround2, backrect)
        if backcount == 3:
            screen.blit(backround3, backrect)
        if backcount == 4:
            screen.blit(backround4, backrect)
        if backcount == 5:
            screen.blit(backround5, backrect)
        if backcount == 6:
            screen.blit(backround6, backrect)
        if backcount == 7:
            screen.blit(backround7, backrect)
        if backcount == 8:
            screen.blit(backround8, backrect)
        if backcount == 9:
            screen.blit(backround9, backrect)
        if backcount == 10:
            screen.blit(backround10, backrect)
        if backcount == 11:
            screen.blit(backround11, backrect)
        if backcount == 12:
            screen.blit(backround12, backrect)
        if backcount == 13:
            screen.blit(backround13, backrect)
        if backcount == 14:
            screen.blit(backround14, backrect)
            backcount = 0

        renderedText = font1.render("You have ten lives that reset each wave", 1, teal)
        screen.blit(renderedText, (75, height - 195))
        renderedText = font1.render("Last as long as you can", 1, teal)
        screen.blit(renderedText, (420, height - 125))
        renderedText = font2.render("Press Space", 1, teal)
        screen.blit(renderedText, (118, 95))

        pygame.display.flip()
        # pygame.time.wait(10)


def game():
    import pygame, sys, random
    import math
    pygame.init()
    pygame.key.set_repeat(10)
    size = width, height = 1680, 1050
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption('Roidz')

    # pygame.mixer.music.load('roidmusic.wav')
    # pygame.mixer.music.play(-1)

    font1 = pygame.font.Font("res/pixelmix_bold.ttf", 51)
    font2 = pygame.font.Font("res/pixelmix_bold.ttf", 222)

    black = [0, 0, 0]
    white = [255, 255, 255]
    green = [0, 255, 0]
    red = [255, 0, 0]
    teal = [0, 155, 255]

    bullets = []
    asteroids = []

    wave = 1
    score = 0
    count = 0
    backcount = 1
    lives = 10
    reload = 0
    bulletSpeed = 20
    maxSpeed = 15
    numAsteroids = 1
    asteroidSize = 160.0
    asteroidspeed = 1

    # determine if a point is inside a given polygon or not
    # from http://www.ariel.com.au/a/python-point-int-poly.html
    # poly is a list of (x,y) pairs.
    def pointInsidePolygon(x, y, poly):
        n = len(poly)
        inside = False
        p1x, p1y = poly[0]
        for i in range(n + 1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    class Ship:
        def __init__(self):
            self.pos = [width / 2, height / 2]
            self.speed = 0
            self.angle = 0
            self.points = [[-5, 0], [-15, -10], [15, 0], [-15, 10]]

        def move(self):
            self.pos[0] = int(self.pos[0] + self.speed * math.cos(self.angle * math.pi / 180)) % width
            self.pos[1] = int(self.pos[1] + self.speed * math.sin(self.angle * math.pi / 180)) % height

        def getShape(self):
            ang = self.angle * math.pi / 180.0
            points = []
            for p in self.points:
                x = p[0] * math.cos(ang) - p[1] * math.sin(ang) + self.pos[0]
                y = p[0] * math.sin(ang) + p[1] * math.cos(ang) + self.pos[1]
                x2 = p[0] * math.cos(ang) - p[1] * math.sin(ang)
                y2 = p[0] * math.sin(ang) + p[1] * math.cos(ang)
                points.append([x, y])
            return points

    class Asteroid:
        def __init__(self, size, pos, speed=None):
            self.size = size
            self.points = []
            for i in range(0, 8):
                ang = math.pi * i / 4
                l = size + random.randint(-int(size / 2), int(size / 2))
                self.points.append([l * math.cos(ang), l * math.sin(ang)])
            self.pos = pos
            if speed == None:
                self.speed = [random.random() * asteroidspeed - 5, random.random() * asteroidspeed - 5]
            else:
                self.speed = speed
            self.angle = 0.0
            self.rotation = random.random() * 2 - 1

        def move(self):
            self.pos[0] = (self.pos[0] + self.speed[0]) % width
            self.pos[1] = (self.pos[1] + self.speed[1]) % height
            self.angle = self.angle + self.rotation

        def getShape(self):
            ang = self.angle * math.pi / 180.0
            points = []
            for p in self.points:
                x = p[0] * math.cos(ang) - p[1] * math.sin(ang) + self.pos[0]
                y = p[0] * math.sin(ang) + p[1] * math.cos(ang) + self.pos[1]
                points.append([x, y])
            return points

    class Bullet:
        def __init__(self, pos, speed):
            self.pos = pos
            self.speed = speed

        def move(self):
            self.pos[0] = int(self.pos[0] + self.speed[0])
            self.pos[1] = int(self.pos[1] + self.speed[1])

    ship = Ship()

    for a in range(0, numAsteroids):
        asteroids.append(Asteroid(asteroidSize, [random.random() * width, 300.50]))

    for b in bullets:
        b.move()
        if b.pos[0] < 0 or b.pos[0] > width or b.pos[1] < 0 or b.pos[1] > height:
            bullets.remove(b)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                ship.angle = ship.angle - 15
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_RIGHT]:
                ship.angle = ship.angle + 15
            if keys[pygame.K_UP]:
                ship.speed = ship.speed + 1
                if ship.speed > maxSpeed:
                    ship.speed = maxSpeed
            if keys[pygame.K_DOWN]:
                ship.speed = ship.speed - 1
                if ship.speed < 0:
                    ship.speed = 0
            if keys[pygame.K_SPACE]:
                if reload > 5:
                    bx = bulletSpeed * math.cos(ship.angle * math.pi / 180)
                    by = bulletSpeed * math.sin(ship.angle * math.pi / 180)
                    bullet = Bullet([ship.pos[0], ship.pos[1]], [bx, by])
                    bullets.append(bullet)
                    reload = 0
            reload = reload + 1

        for p in ship.getShape():
            for a in asteroids:
                if pointInsidePolygon(p[0], p[1], a.getShape()):
                    asteroids.remove(a)
                    lives = lives - 1
                    score = score - 150
                    break

        for a in asteroids:
            a.move()

        for b in bullets:
            b.move()
            if b.pos[0] < 0 or b.pos[0] > width or b.pos[1] < 0 or b.pos[1] > height:
                bullets.remove(b)

        ship.move()

        for b in bullets:
            for a in asteroids:
                if pointInsidePolygon(b.pos[0], b.pos[1], a.getShape()):
                    bullets.remove(b)
                    asteroids.remove(a)
                    score = score + 100
                    if a.size > 40:
                        new = Asteroid(int(a.size / 2), [a.pos[0], a.pos[1]], [a.speed[0], a.speed[1]])
                        asteroids.append(new)
                        new = Asteroid(int(a.size / 2), [a.pos[0], a.pos[1]], [a.speed[1], a.speed[0]])
                        asteroids.append(new)
                        new = Asteroid(int(a.size / 2), [a.pos[0], a.pos[1]], [-a.speed[0], a.speed[1]])
                        asteroids.append(new)
                        new = Asteroid(int(a.size / 2), [a.pos[0], a.pos[1]], [-a.speed[1], a.speed[0]])
                        asteroids.append(new)
                    break

        if lives == 0:
            lose()

        if lives == 3:
            green = [255, 0, 0]
        if lives == 6:
            green = [255, 255, 0]
        if lives >= 7:
            green = [0, 255, 0]

        backcount = backcount + 1
        if backcount == 1:
            screen.blit(backround, backrect)
        if backcount == 2:
            screen.blit(backround2, backrect)
        if backcount == 3:
            screen.blit(backround3, backrect)
        if backcount == 4:
            screen.blit(backround4, backrect)
        if backcount == 5:
            screen.blit(backround5, backrect)
        if backcount == 6:
            screen.blit(backround6, backrect)
        if backcount == 7:
            screen.blit(backround7, backrect)
        if backcount == 8:
            screen.blit(backround8, backrect)
        if backcount == 9:
            screen.blit(backround9, backrect)
        if backcount == 10:
            screen.blit(backround10, backrect)
        if backcount == 11:
            screen.blit(backround11, backrect)
        if backcount == 12:
            screen.blit(backround12, backrect)
        if backcount == 13:
            screen.blit(backround13, backrect)
        if backcount == 14:
            screen.blit(backround14, backrect)
            backcount = 0
        if count >= 15 or len(asteroids) == 0:
            numAsteroids = numAsteroids + 1
            for a in range(0, numAsteroids):
                asteroids.append(Asteroid(asteroidSize, [random.random() * width, 50.0]))
            count = 0
            lives = 10
            score = score + 250
            wave = wave + 1

        pygame.draw.polygon(screen, green, ship.getShape(), 1)
        for a in asteroids:
            pygame.draw.polygon(screen, green, a.getShape(), 1)

        for b in bullets:
            pygame.draw.circle(screen, red, b.pos, 5, 0)

        for x in range(0, lives):
            rct = pygame.Rect(10 + x * 40, height - 25, 35, 25)
            pygame.draw.rect(screen, green, rct, 0)

        renderedText = font1.render("Score: " + str(score), 1, white)
        screen.blit(renderedText, (10, 10))
        renderedText = font1.render("Wave: " + str(wave), 1, white)
        screen.blit(renderedText, (1350, 10))

        count = count + .01
        pygame.display.flip()
        # pygame.time.wait(10)


start()
