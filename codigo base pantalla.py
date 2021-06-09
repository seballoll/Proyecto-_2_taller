import sys,pygame
from random import randint
from pygame.locals import *

clock = pygame.time.Clock()
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
pygame.display.set_caption('NINJA BOI')
fontoftitle = pygame.font.Font(None, 40)
fontofsubtitle = pygame.font.Font(None, 30)
fontofhp = pygame.font.Font(None, 30)

# Texts
textoftitle = fontoftitle.render("Operation Moon Light", 0, (255, 255, 255))
textofsubtitle = fontofsubtitle.render("Entry your name", 0, (255, 255, 255))
textofindication = fontofsubtitle.render("(Write a short name)", 0, (255, 255, 255))
textoflvl1 = fontofsubtitle.render("Level1", 0, (255, 255, 255))
textoflvl2 = fontofsubtitle.render("Level2", 0, (255, 255, 255))
textoflvl3 = fontofsubtitle.render("Level3", 0, (255, 255, 255))
textofinstructions = fontofsubtitle.render("Instructions", 0, (255, 255, 255))
textofaboutinfo = fontofsubtitle.render("About", 0, (255, 255, 255))
textofleaderboard = fontofsubtitle.render("Leaderboard", 0, (255, 255, 255))



# ------------------------------------------ Function of the principal screen ---------------------------------------#

# initial values
clickbutton = False
active = False


def mainscreen():
    # initial values
    clickbutton = False
    active = False
    usertext = ''
    while True:
        screen.fill((0, 0, 0)) # to fill the screen

        mx, my = pygame.mouse.get_pos()

        level1 = pygame.Rect(175, 200, 150, 25)
        level2 = pygame.Rect(175, 250, 150, 25)
        level3 = pygame.Rect(175, 300, 150, 25)
        instructions = pygame.Rect(175, 350, 150, 25)
        about = pygame.Rect(175, 400, 150, 25)
        leaderboard = pygame.Rect(175, 450, 150, 25)
        # rectangles of the principal screen positions and dimensions on x,y

        if level1.collidepoint((mx, my)):
            if clickbutton:
                screenlevel1()
        if level2.collidepoint((mx, my)):
            if clickbutton:
                screenlevel2()
        if level3.collidepoint((mx, my)):
            if clickbutton:
                screenlevel3()
        if instructions.collidepoint((mx, my)):
            if clickbutton:
                screeninstructions()
        if about.collidepoint((mx, my)):
            if clickbutton:
                aboutscreen()
        if leaderboard.collidepoint((mx, my)):
            if clickbutton:
                screenleaderboard()
            # when u click the rectangle that we created before it takes u to a different screen

        pygame.draw.rect(screen, (255, 0, 0), level1)
        pygame.draw.rect(screen, (255, 0, 0), level2)
        pygame.draw.rect(screen, (255, 0, 0), level3)
        pygame.draw.rect(screen, (255, 0, 0), instructions)
        pygame.draw.rect(screen, (255, 0, 0), about)
        pygame.draw.rect(screen, (255, 0, 0), leaderboard)
        # it draws the rectangles with the red colors

        # initial values
        clickbutton = False
        active = True

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN: # to go to the last screen
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.quit()

            if event.type == MOUSEBUTTONDOWN:  # if it's 1 it's true and it takes u to the screen
                if event.button == 1:
                    clickbutton = True

            if event.type == pygame.MOUSEBUTTONDOWN:  # when you press the button you can write your name
                if inputrectangle.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:  # it allows you to delete letters
                        usertext = usertext[:-1]
                    else:
                        usertext += event.unicode

        fontofname = pygame.font.Font(None, 25)
        inputrectangle = pygame.Rect(150, 125, 200, 25)
        color1 = pygame.Color('brown1')  # color for the rectangle where u write your name
        active = True

        pygame.draw.rect(screen, color1, inputrectangle)
        textsurface = fontofname.render(usertext, True, (255, 255, 255))
        screen.blit(textsurface, (inputrectangle.x + 5, inputrectangle.y + 5))
        inputrectangle.w = max(150, textsurface.get_width() + 10)

        screen.blit(textoftitle, (100, 50))  # it writes the titles of the rectangles
        screen.blit(textofsubtitle, (175, 100))
        screen.blit(textofindication, (160, 165))
        screen.blit(textoflvl1, (220, 205))
        screen.blit(textoflvl2, (220, 255))
        screen.blit(textoflvl3, (220, 305))
        screen.blit(textofinstructions, (190, 355))
        screen.blit(textofaboutinfo, (225, 405))
        screen.blit(textofleaderboard, (190, 455))
        pygame.display.update()
        clock.tick(60)

def screenlevel1():
    pygame.display.set_caption('Level 1')  # title
    playing = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # to go to the last screen
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        print("izquierda")
                        Ninja.speed = [-1, 0]
                    elif keys[pygame.K_RIGHT]:
                        print("derecha")
                        Ninja.speed = [1, 0]
                    elif keys[pygame.K_DOWN]:
                        print("abajo")
                        Ninja.speed = [0, 1]
                    elif keys[pygame.K_UP]:
                        print("arriba")
                        Ninja.speed = [0, -1]
                    running = False
                    mainscreen()
                    pygame.display.set_caption('NINJA BOI')

        Ninja.ninjarect = Ninja.ninjarect.move(Ninja.speed)
        Shuriken.shurikenrect = Shuriken.shurikenrect.move(Shuriken.speed)
        pygame.time.delay(5)

        if playing == True:
            check_border.check(check_border)

        screen.fill(black)
        screen.blit(Ninja.ninja, Ninja.ninjarect)
        screen.blit(Shuriken.shuriken, Shuriken.shurikenrect)
        pygame.display.update()
        clock.tick(60)

def screenlevel2(usertext):
    pygame.display.set_caption('Level 2')  # title

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # to go to the last screen
                    running = False
                    mainscreen()
                    pygame.display.set_caption('NINJA BOI')

        pygame.display.update()
        clock.tick(60)

def screenlevel3(usertext, score):
    pygame.display.set_caption('Level 3')  # title

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # to go to the last screen
                    running = False
                    mainscreen()
                    pygame.display.set_caption('NINJA BOI')

        pygame.display.update()
        clock.tick(60)

def screeninstructions():
    pygame.display.set_caption('Instructions')  # title

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # to go to the last screen
                    running = False
                    mainscreen()
                    pygame.display.set_caption('NINJA BOI')

        pygame.display.update()
        clock.tick(60)

def aboutscreen():
    pygame.display.set_caption('About')  # title

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # to go to the last screen
                    running = False
                    mainscreen()
                    pygame.display.set_caption('NINJA BOI')

        pygame.display.update()
        clock.tick(60)

def screenleaderboard(usertext, score):
    pygame.display.set_caption('Leaderboard')  # title

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # to go to the last screen
                    running = False
                    mainscreen()
                    pygame.display.set_caption('NINJA BOI')


        pygame.display.update()
        clock.tick(60)