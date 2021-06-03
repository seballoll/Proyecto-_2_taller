import sys,pygame
pygame.init()
class Ninja:
    ball = pygame.image.load("2nd boss.png")
    ballrect = ball.get_rect()
    ballrect.update(40, 40, 70, 70)
    speed = [1, 1]



black = 0, 0, 0
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
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
    Ninja.ballrect = Ninja.ballrect.move(Ninja.speed)
    pygame.time.delay(5)

    screen.fill(black)
    screen.blit(Ninja.ball, Ninja.ballrect)
    pygame.display.flip()