import sys,pygame
from random import randint
pygame.init()

class Ninja:
    ninja = pygame.image.load("ninja .png")
    ninjarect = ninja.get_rect()
    print(ninjarect)
    ninjarect.update(200, 200, 270, 270)
    speed = [1, 1]
class Shuriken:
    shuriken = pygame.image.load("shuriken.png")
    shurikenrect = shuriken.get_rect()
    shurikenrect.update(0,0,50,26)
    speed = [1,0]
    def bounce_positive(self):
        return randint(0,1)
    def bounce_negative(self):
        return randint(-1,0)
    def bounce_random(self):
        return randint(-1,1)
class check_border:
    def check(self):
        if Ninja.ninjarect.left <= 0:
            Ninja.speed = [1, 0]
        if Ninja.ninjarect.right >= 900:
            Ninja.speed = [-1, 0]
        if Ninja.ninjarect.top <= 0:
            Ninja.speed = [0, 1]
        if Ninja.ninjarect.bottom >= 890:
            Ninja.speed = [0, -1]
        if Shuriken.shurikenrect.left <= 0:
            Shuriken.speed = [Shuriken.bounce_positive(Shuriken), Shuriken.bounce_random(Shuriken)]
            print("a")
        if Shuriken.shurikenrect.right >= 750:
            Shuriken.speed = [Shuriken.bounce_negative(Shuriken),Shuriken.bounce_random(Shuriken)]
            print("e")
        if Shuriken.shurikenrect.top <= 0:
            Shuriken.speed = [Shuriken.bounce_random(Shuriken), Shuriken.bounce_positive(Shuriken)]
            print("i")
        if Shuriken.shurikenrect.bottom >= 700:
            Shuriken.speed = [Shuriken.bounce_random(Shuriken), Shuriken.bounce_negative(Shuriken)]
            print("o")

black = 100, 100, 100
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
playing = True
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                print("izquierda")
                Ninja.speed = [-1,0]
            elif keys[pygame.K_RIGHT]:
                print("derecha")
                Ninja.speed = [1,0]
            elif keys[pygame.K_DOWN]:
                print("abajo")
                Ninja.speed = [0,1]
            elif keys[pygame.K_UP]:
                print("arriba")
                Ninja.speed = [0,-1]


    Ninja.ninjarect = Ninja.ninjarect.move(Ninja.speed)
    Shuriken.shurikenrect = Shuriken.shurikenrect.move(Shuriken.speed)
    pygame.time.delay(5)

    if playing == True:

        check_border.check(check_border)

    screen.fill(black)
    screen.blit(Ninja.ninja, Ninja.ninjarect)
    screen.blit(Shuriken.shuriken, Shuriken.shurikenrect)
    pygame.display.flip()