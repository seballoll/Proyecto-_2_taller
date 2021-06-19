# General Setup: we call the librarie to start programming the game
import pygame, sys
import random  # so we can manipulate the random number that the enemy throws
from pygame.locals import *

# Principal Window Setup
pygame.init()
clock = pygame.time.Clock()  # function for the timer
timer = 0  # inital value
PRINCIPALSCREEN1 = pygame.display.set_mode([700, 700])  # to pop up the screen
pygame.display.set_caption('Ninja Dash')  # title
icon1 = pygame.image.load("ninja .png") # icon
pygame.display.set_icon(icon1)


# -------------------------------------------Text for the principal window---------------------------------------#

# Fonts of the text
fontoftitle = pygame.font.Font(None, 40)
fontofsubtitle = pygame.font.Font(None, 30)
fontofhp = pygame.font.Font(None, 30)

# Texts
textoftitle = fontoftitle.render("手裏剣物語", 0, (255, 255, 255))
textofsubtitle = fontofsubtitle.render("Entry your name", 0, (255, 255, 255))
textofindication = fontofsubtitle.render("(Write a short name)", 0, (255, 255, 255))
textoflvl1 = fontofsubtitle.render("Level1", 0, (0, 0, 0))
textoflvl2 = fontofsubtitle.render("Level2", 0, (0, 0, 0))
textoflvl3 = fontofsubtitle.render("Level3", 0, (0, 0, 0))
textofinstructions = fontofsubtitle.render("Instructions", 0, (0, 0, 0))
textofaboutinfo = fontofsubtitle.render("About", 0, (0, 0, 0))
textofleaderboard = fontofsubtitle.render("Leaderboard", 0, (0, 0, 0))

# ------------------------------------------ Background images class -----------------------------------------------#


class backgroun_image:
    def __init__(self,level):
        self.level = level
        self.bg1 = pygame.image.load("bamboo forest.jpg")
        self.bg2 = pygame.image.load("sakura forest.jpg")
        self.bg3 = pygame.image.load("torii.jpg")
    def choose_level(self):
        if self.level == 1:
            return self.bg1
        elif self.level ==2:
            return  self.bg2
        elif self.level == 3:
            return self.bg3

# ------------------------------------------ Function of the principal screen -----------------------------------------#

# initial values
clickbutton = False
active = False

# GLOBAL SCORE
score = 0

def mainscreen():
    # initial values
    clickbutton = False
    active = False
    usertext = ''
    bg1 = pygame.image.load("dojo.jpg")
    while True:
        PRINCIPALSCREEN1.fill((0, 0, 0)) # to fill the screen

        mx, my = pygame.mouse.get_pos()

        level1 = pygame.Rect(75, 200, 150, 25)
        level2 = pygame.Rect(75, 250, 150, 25)
        level3 = pygame.Rect(75, 300, 150, 25)
        instructions = pygame.Rect(75, 350, 150, 25)
        about = pygame.Rect(75, 400, 150, 25)
        leaderboard = pygame.Rect(75, 450, 150, 25)
        PRINCIPALSCREEN1.blit(bg1,(0,0))
        # rectangles of the principal screen positions and dimensions on x,y

        if level1.collidepoint((mx, my)):
            if clickbutton:
                screenlevel1(usertext)
        if level2.collidepoint((mx, my)):
            if clickbutton:
                screenlevel2(usertext)
        if level3.collidepoint((mx, my)):
            if clickbutton:
                screenlevel3(usertext, score)
        if instructions.collidepoint((mx, my)):
            if clickbutton:
                screeninstructions()
        if about.collidepoint((mx, my)):
            if clickbutton:
                aboutscreen()
        if leaderboard.collidepoint((mx, my)):
            if clickbutton:
                screenleaderboard(usertext, score)
        # when u click the rectangle that we created before it takes u to a different screen

        pygame.draw.rect(PRINCIPALSCREEN1, (255, 255, 255), level1)
        pygame.draw.rect(PRINCIPALSCREEN1, (255, 255, 255), level2)
        pygame.draw.rect(PRINCIPALSCREEN1, (255, 255, 255), level3)
        pygame.draw.rect(PRINCIPALSCREEN1, (255, 255, 255), instructions)
        pygame.draw.rect(PRINCIPALSCREEN1, (255, 255, 255), about)
        pygame.draw.rect(PRINCIPALSCREEN1, (255, 255, 255), leaderboard)
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
        inputrectangle = pygame.Rect(50, 125, 200, 25)
        color1 = pygame.Color(0,  0, 0)  # color for the rectangle where u write your name
        active = True

        pygame.draw.rect(PRINCIPALSCREEN1, color1, inputrectangle)
        textsurface = fontofname.render(usertext, True, (255, 255, 255))
        PRINCIPALSCREEN1.blit(textsurface, (inputrectangle.x + 5, inputrectangle.y + 5))
        inputrectangle.w = max(50, textsurface.get_width() + 10)
        PRINCIPALSCREEN1.blit(textoftitle, (125, 50))  # it writes the titles of the rectangles
        PRINCIPALSCREEN1.blit(textofsubtitle, (50, 100))
        PRINCIPALSCREEN1.blit(textofindication, (50, 165))
        PRINCIPALSCREEN1.blit(textoflvl1, (120, 205))
        PRINCIPALSCREEN1.blit(textoflvl2, (120, 255))
        PRINCIPALSCREEN1.blit(textoflvl3, (120, 305))
        PRINCIPALSCREEN1.blit(textofinstructions, (90, 355))
        PRINCIPALSCREEN1.blit(textofaboutinfo, (125, 405))
        PRINCIPALSCREEN1.blit(textofleaderboard, (90, 455))
        pygame.display.update()
        clock.tick(60)

# -------------------GAME CONFIG-------------------------


NINJAGOTHIT = pygame.USEREVENT  # event when the ninja get damage
NINJA_HEALTH = 50
# ----------------------------------------------- Ninja Class    -------------------------------------------------#
class Ninja:

        Ninja_image = pygame.image.load("ninja .png")
        Ninja = pygame.transform.scale(Ninja_image, (50, 50))
        speed = [1,0]
# ----------------------------------------------- Shuriken Class -------------------------------------------------#
class Shuriken:  # class of the enemy
    Shuriken_image = pygame.image.load("shuriken.png")
    shurikenrect = Shuriken_image.get_rect()
    shurikenrect.update(5, 5, 55, 31)
    speed = [1, 0]
    def bounce_positive(self):
        return random.randint(0, 1)

    def bounce_negative(self):
        return random.randint(-1, 0)

    def bounce_random(self):
        return random.randint(-1, 1)
# -----------------------------------Function for the movement of baby yoda---------------------------------------#


def ninja_movement(keysmovement, ninja):
    if keysmovement[pygame.K_w] and ninja.y - 5 > 0:  # going up when u press W
        ninja.y -= 5
    if keysmovement[pygame.K_s] and ninja.y + 5 + 50 < 700:  # going down when u press D
        ninja.y += 5
    if keysmovement[pygame.K_a] and ninja.x - 5 > 0:  # going left when u press A
        ninja.x -= 5
    if keysmovement[pygame.K_d] and ninja.x + 50 < 500:  # going right when u press D
        ninja.x += 5

# ---------------------------------Function to draw all the variables of the levels-------------------------------#


def drawscreen(ninja, NINJA_HEALTH, usertext, currenttime, level):
    background_image = backgroun_image(level)
    PRINCIPALSCREEN1.blit(background_image.choose_level(),(0,0))
    ninja_health = fontofhp.render("LIFE:" + str(NINJA_HEALTH), 1, (232, 54, 0))
    usertext = fontofhp.render("NAME:" + str(usertext), 1, (232, 54, 0))
    scoretext = fontofhp.render("SCORE:" + str(score), 1, (232, 54, 0))
    currenttime1 = fontofhp.render("TIME:" + str(currenttime), 1, (232, 54, 0))
    # text of the variables on levels screen
    PRINCIPALSCREEN1.blit(ninja_health, (10, 650))
    PRINCIPALSCREEN1.blit(usertext, (230, 650))
    PRINCIPALSCREEN1.blit(scoretext, (20, 20))
    PRINCIPALSCREEN1.blit(currenttime1, (400, 20))  # it writes the text
    PRINCIPALSCREEN1.blit(Ninja.Ninja_image, (ninja.x, ninja.y))
    PRINCIPALSCREEN1.blit(Shuriken.Shuriken_image, (Shuriken.shurikenrect))

    pygame.display.update()


# --------------Function for the movement of Darth Vader in the first and third level--------------------#
'''def darthvadermoving(darthvader, DARTHVADERVELOCITY, ATTACKVELOCITY, babyyoda):
    if darthvader.attack == False:  # it moves to the right and to the left constantly
        if darthvader.x - DARTHVADERVELOCITY <= 0 and darthvader.left == True:
            darthvader.left = False  # if it's too close to the left border it starts to move right
        if darthvader.x + DARTHVADERVELOCITY + 50 >= 500 and darthvader.left == False:
            darthvader.left = True  # if it's too close to the right border it starts to move left
        elif darthvader.left:
            darthvader.x -= DARTHVADERVELOCITY
        elif darthvader.left == False:
            darthvader.x += DARTHVADERVELOCITY
    else:
        if darthvader.readycharge == True:
            if darthvader.y - ATTACKVELOCITY <= 50 and darthvader.invading == False:
                darthvader.invading = True  # if it's at the first part it start charging
                darthvader.attack = False
                darthvader.charge = False
                darthvader.readycharge = False
                darthvader.timer = 0
            if darthvader.y + ATTACKVELOCITY + 50 >= 700 and darthvader.invading == True:
                darthvader.invading = False  # if it's too close to the border it goes backwards
                global DARTH_VADER_HEALTH
                DARTH_VADER_HEALTH -= 1 # and when that happens it decreases darth vader's life
            elif darthvader.invading == False:
                darthvader.y -= ATTACKVELOCITY
                if darthvader.x < babyyoda.x < darthvader.x + 50 and darthvader.y < babyyoda.y < darthvader.y + 50:
                    global BABY_YODA_HEALTH
                    BABY_YODA_HEALTH -= 10  # if it's going down and touch baby yoda it decreases his life
            elif darthvader.invading == True:
                darthvader.y += ATTACKVELOCITY
                if darthvader.x < babyyoda.x < darthvader.x + 50 and darthvader.y < babyyoda.y < darthvader.y + 50:
                    BABY_YODA_HEALTH -= 10  # if it's going up and touch baby yoda it decreases his life

# -------------------------------Function for the charge in the first level-----------------------------------------#
def attack(darthvader, ATTACKVELOCITY):
    if darthvader.timer == 120 and darthvader.charge == False:
        darthvader.timer = 0  # recursivity
        if random.randint(1, 10) % 3 == 0:  #picks a random number and it determinate if it's divisble by 3
            darthvader.charge = True # charges if it's divisible
            darthvader.attack = True
    elif darthvader.timer == 30 and darthvader.charge == True:
        darthvader.readycharge = True  # if both are true it cahrges
    else:
        darthvader.timer += 1
'''

# -----------------------------------------Function for the level 1 screen---------------------------------------#
# GLOBAL SCORE
score = 0


def screenlevel1(usertext):
    # calls global values
    global score, NINJA_HEALTH, Ninja_image
    score = 0
#    Ninja_image = pygame.image.load("ninja .png")
#    ninja = pygame.transform.scale(Ninja_image, (50, 50))
    ninja = pygame.Rect(225, 600, 50, 50)  # rectangle to manipulate the ninja
    shuriken = Shuriken.Shuriken_image.get_rect()  # to manipulate the enemy cause it can't be rect
    NINJA_HEALTH = 50  # HP of the player
    pygame.display.set_caption('Level 1') # title
    currenttime = 0
    timer = 0  # initial values
    running = True
    while running:
        PRINCIPALSCREEN1.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # to go to the last screen with ESCAPE
                if event.key == K_ESCAPE:
                    running = False
                    pygame.display.set_caption('Operation Moon light')  # puts the title

            if event.type == NINJAGOTHIT: # if the ninja gets damage it decreases it's life life
                NINJA_HEALTH -=1

        if NINJA_HEALTH <= 0: # if u die it takes you to the main screen
            mainscreen()
            flag = 0

        Shuriken.shurikenrect = Shuriken.shurikenrect.move(Shuriken.speed)

        if timer == 60: # timer
            timer = 0
            currenttime += 1
        else:
            timer += 1

        if Shuriken.shurikenrect.left <= 0:
            Shuriken.speed = [Shuriken.bounce_positive(Shuriken), Shuriken.bounce_random(Shuriken)]

        if Shuriken.shurikenrect.right >= 750:
            Shuriken.speed = [Shuriken.bounce_negative(Shuriken),Shuriken.bounce_random(Shuriken)]

        if Shuriken.shurikenrect.top <= 0:
            Shuriken.speed = [Shuriken.bounce_random(Shuriken), Shuriken.bounce_positive(Shuriken)]

        if Shuriken.shurikenrect.bottom >= 700:
            Shuriken.speed = [Shuriken.bounce_random(Shuriken), Shuriken.bounce_negative(Shuriken)]

        keysmovement = pygame.key.get_pressed()
        ninja_movement(keysmovement, ninja)
        drawscreen(ninja, NINJA_HEALTH, usertext, currenttime, 1)
        pygame.display.update()
        clock.tick(60)  # recursivity of the functions every 60 FPS


# ----------------------------------------Function for the level 2 function--------------------------------------------#
# GLOBAL SCORE
score = 0


def screenlevel2(usertext, score2 = 0):

    global score, NINJA_HEALTH
    score = 0
    ninja = pygame.Rect(225, 600, 50, 50)  # rectangle to manipulate the spaceship
    shuriken = Shuriken.Shuriken_image.get_rect()  # to manipulate the enemy cause it can't be rect
    NINJA_HEALTH = 50  # HP of the player
    pygame.display.set_caption('Level 2') # title
    currenttime = 0
    timer = 0  # initial values
    running = True
    while running:
        PRINCIPALSCREEN1.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # to go to the last screen
                    running = False
                    pygame.display.set_caption('Operation Moon light')

            if event.type == NINJAGOTHIT:  # when the ninja gets hit it decreases the ninja's life
                NINJA_HEALTH -=1

            if NINJA_HEALTH <= 0:  # if you die it goes back to the primcipal screen
                mainscreen()
                flag = 0

        if timer == 60:  # function of the timer
            timer = 0
            currenttime += 1
        else:
            timer += 1

        keysmovement = pygame.key.get_pressed()
        ninja_movement(keysmovement, ninja)
        drawscreen(ninja, NINJA_HEALTH, usertext, currenttime, 2)
        pygame.display.update()
        clock.tick(60)  # all of the functions called are in the while so they do the recursivity

# --------------------------------------Function for the level 3 screen----------------------------------------------#
# GLOBAL SCORE
score = 0


def screenlevel3(usertext, score3):

    global score, NINJA_HEALTH
    score = 0

    ninja = pygame.Rect(225, 600, 50, 50)  # rectangle to manipulate the ninja
    shuriken = Shuriken.Shuriken_image.get_rect()  # to manipulate the enemy cause it can't be rect
    NINJA_HEALTH = 50  # HP of the player
    darth_vader_bullets = []
    pygame.display.set_caption('Level 3') # title
    currenttime = 0
    timer = 0  # initial values
    running = True
    while running:
        PRINCIPALSCREEN1.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # to go to the last screen
                    running = False
                    mainscreen()
                    pygame.display.set_caption('Operation Moon light')

            if event.type == NINJAGOTHIT:  # when the player got hit it decreases to the player's HP
                NINJA_HEALTH -= 10

            if NINJA_HEALTH <= 0:  # if you die it goes back to the principal screen
                mainscreen()
                flag = 0

        if timer == 60:  # function of the timer
            timer = 0
            currenttime += 1
        else:
            timer += 1

        keysmovement = pygame.key.get_pressed()
        ninja_movement(keysmovement, ninja)
        drawscreen(ninja, NINJA_HEALTH, usertext, currenttime, 3)
        pygame.display.update()
        clock.tick(60)  # all of the functions called are in the while so they do the recursivity


# ------------------------------------------Text for the instructions window-----------------------------------------#
fontoftitle = pygame.font.Font(None, 40)
fontofsubtitle = pygame.font.Font(None, 30)
textoftitle2 = fontoftitle.render("Instructions", 0, (255, 255, 255))
textofspam = fontofsubtitle.render("Select: About to know about the developers", 0, (255, 255, 255))
textoflevel = fontofsubtitle.render("Select the level you want to play", 0, (255, 255, 255))
textofwasd = fontofsubtitle.render("Move with w,a,s,d to move", 0, (255, 255, 255))
textofmovement = fontofsubtitle.render("front,left,back and right", 0, (255, 255, 255))
textofalert = fontofsubtitle.render("avoid to get hit by any shuriken", 0, (255, 255, 255))
textofadvice = fontofsubtitle.render("the levels will get harder so stay alert", 0, (255, 255, 255))
textofscorentime = fontofsubtitle.render("your score and the time will show in the screen", 0, (255, 255, 255))
textoflastline = fontofsubtitle.render("while you're playing", 0, (255, 255, 255))

# ---------------------------------------Function for the istructions screen----------------------------------------#


def screeninstructions():
    pygame.display.set_caption('Instructions')  # title
    running = True
    while running:
        PRINCIPALSCREEN1.fill((0, 0, 0))  # to fill the screen
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # to go to the last screen
                    running = False
                    pygame.display.set_caption('Operation Moon light')

# It writes the text on a posicion x,y
        PRINCIPALSCREEN1.blit(textoftitle2, (250, 50))
        PRINCIPALSCREEN1.blit(textofspam, (130, 100))
        PRINCIPALSCREEN1.blit(textoflevel, (180, 150))
        PRINCIPALSCREEN1.blit(textofwasd, (200, 200))
        PRINCIPALSCREEN1.blit(textofmovement, (210, 250))
        PRINCIPALSCREEN1.blit(textofalert, (180, 300))
        PRINCIPALSCREEN1.blit(textofadvice, (140, 350))
        PRINCIPALSCREEN1.blit(textofscorentime, (100, 400))
        PRINCIPALSCREEN1.blit(textoflastline, (240, 450))

        pygame.display.update()
        clock.tick(60)


# ------------------------------------------Text for the about window-----------------------------------------#
# Fonts for the about screen's text
fontoftitle = pygame.font.Font(None, 40)
fontofsubtitle = pygame.font.Font(None, 30)
textoftitle1 = fontoftitle.render("About", 0, (255, 255, 255))
textofstudent1 = fontofsubtitle.render("Student: Sebastián Manyusly Chen Cerdas", 0, (255, 255, 255))
textofstudent2 = fontofsubtitle.render("& Abraham Venegas Mayorga", 0, (255, 255, 255))
textofteacher = fontofsubtitle.render("Teacher: Luis Barboza Artavia", 0, (255, 255, 255))
textofcourse = fontofsubtitle.render("Programming Workshop", 0, (255, 255, 255))
textofcr = fontofsubtitle.render("Costa Rican Videogame", 0, (255, 255, 255))
textofGroup = fontofsubtitle.render("Group 4", 0, (255, 255, 255))
textofU = fontofsubtitle.render("TEC", 0, (255, 255, 255))
textofyear = fontofsubtitle.render("2021", 0, (255, 255, 255))
textofversion = fontofsubtitle.render("pygame 2.0.1 (SDL 2.0.14, Python 3.8.5)", 0, (255, 255, 255))
textofce = fontofsubtitle.render("Computer Engineering", 0, (255, 255, 255))

# ----------------------------------------Function for the About Screen------------------------------------------#
def aboutscreen():
    pygame.display.set_caption('About')  # title of the window
    running = True
    while running:
        PRINCIPALSCREEN1.fill((0, 0, 0))  # to fill the screen

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # to go to the last screen
                    running = False
                    pygame.display.set_caption('Operation Moon light')

# It writes the text on the posicion x, y
        PRINCIPALSCREEN1.blit(textoftitle1, (300, 50))
        PRINCIPALSCREEN1.blit(textofversion, (150, 100))
        PRINCIPALSCREEN1.blit(textofstudent1, (150, 150))
        PRINCIPALSCREEN1.blit(textofstudent2, (200, 200))
        PRINCIPALSCREEN1.blit(textofteacher, (200, 250))
        PRINCIPALSCREEN1.blit(textofce, (225, 300))
        PRINCIPALSCREEN1.blit(textofcourse, (225, 350))
        PRINCIPALSCREEN1.blit(textofcr, (225, 400))
        PRINCIPALSCREEN1.blit(textofGroup, (300, 450))
        PRINCIPALSCREEN1.blit(textofU, (315, 500))
        PRINCIPALSCREEN1.blit(textofyear, (315, 550))

        pygame.display.update()
        clock.tick(60)


# ----------------------------------Function for the top 5 leaderboard-------------------------------------------#
# GLOBAL SCORE
score = 0
def screenleaderboard(usertext, score):
    pygame.display.set_caption('Leaderboard')  # to write the Title
    running = True
    while running:
        PRINCIPALSCREEN1.fill((0, 0, 0))  # to fill with white the background

        for event in pygame.event.get():
            if event.type == QUIT:  # this quits the game
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # this function takes you to the last screen when u hit space
                if event.key == K_ESCAPE:
                    running = False
                    pygame.display.set_caption('Operation Moon light')

        pygame.display.update()  # updates every 60 FPS
        clock.tick(60)

mainscreen()