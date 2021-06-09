# General Setup: we call the librarie to start programming the game
import pygame, sys
import random  # so we can manipulate the random number that the enemy throws
from pygame.locals import *

# Principal Window Setup
pygame.init()
clock = pygame.time.Clock()  # function for the timer
timer = 0  # inital value
PRINCIPALSCREEN1 = pygame.display.set_mode([500, 700])  # to pop up the screen
pygame.display.set_caption('Operation Moon light')  # title
icon1 = pygame.image.load("photos/darth vader.png") # icon
pygame.display.set_icon(icon1)


# -------------------------------------------Text for the principal window---------------------------------------#

# Fonts of the text
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
    while True:
        PRINCIPALSCREEN1.fill((0, 0, 0)) # to fill the screen

        mx, my = pygame.mouse.get_pos()

        level1 = pygame.Rect(175, 200, 150, 25)
        level2 = pygame.Rect(175, 250, 150, 25)
        level3 = pygame.Rect(175, 300, 150, 25)
        instructions = pygame.Rect(175, 350, 150, 25)
        about = pygame.Rect(175, 400, 150, 25)
        leaderboard = pygame.Rect(175, 450, 150, 25)
        #rectangles of the principal screen positions and dimensions on x,y

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

        pygame.draw.rect(PRINCIPALSCREEN1, (255, 0, 0), level1)
        pygame.draw.rect(PRINCIPALSCREEN1, (255, 0, 0), level2)
        pygame.draw.rect(PRINCIPALSCREEN1, (255, 0, 0), level3)
        pygame.draw.rect(PRINCIPALSCREEN1, (255, 0, 0), instructions)
        pygame.draw.rect(PRINCIPALSCREEN1, (255, 0, 0), about)
        pygame.draw.rect(PRINCIPALSCREEN1, (255, 0, 0), leaderboard)
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

        pygame.draw.rect(PRINCIPALSCREEN1, color1, inputrectangle)
        textsurface = fontofname.render(usertext, True, (255, 255, 255))
        PRINCIPALSCREEN1.blit(textsurface, (inputrectangle.x + 5, inputrectangle.y + 5))
        inputrectangle.w = max(150, textsurface.get_width() + 10)

        PRINCIPALSCREEN1.blit(textoftitle, (100, 50))  # it writes the titles of the rectangles
        PRINCIPALSCREEN1.blit(textofsubtitle, (175, 100))
        PRINCIPALSCREEN1.blit(textofindication, (160, 165))
        PRINCIPALSCREEN1.blit(textoflvl1, (220, 205))
        PRINCIPALSCREEN1.blit(textoflvl2, (220, 255))
        PRINCIPALSCREEN1.blit(textoflvl3, (220, 305))
        PRINCIPALSCREEN1.blit(textofinstructions, (190, 355))
        PRINCIPALSCREEN1.blit(textofaboutinfo, (225, 405))
        PRINCIPALSCREEN1.blit(textofleaderboard, (190, 455))
        pygame.display.update()
        clock.tick(60)

#-------------------SPACESHIP CONFIG-------------------------
BABY_YODA_SPACESHIP_IMAGE = pygame.image.load("photos/babyyoda.png")
BABY_YODA_SPACESHIP = pygame.transform.scale(BABY_YODA_SPACESHIP_IMAGE, (50, 50))
DARTH_VADER_IMAGE = pygame.image.load("photos/darth vader.png")
DARTH_VADER = pygame.transform.scale(DARTH_VADER_IMAGE, (50, 50))  # to scale the photos
DARTHVADERGOTHIT = pygame.USEREVENT  # event when darth vader get damage
YODAGOTHIT = pygame.USEREVENT + 2   # event when baby yoda get damage
DARTH_VADER_HEALTH = 30 # values of the HP of the objects
BABY_YODA_HEALTH = 50

# -----------------------------------Function for the movement of baby yoda---------------------------------------#
def baby_yoda_movement(keysmovement, babyyoda):
    if keysmovement[pygame.K_w] and babyyoda.y - 5 > 0:  # going up when u press W
        babyyoda.y -= 5
    if keysmovement[pygame.K_s] and babyyoda.y + 5 + 50 < 700:  # going down when u press D
        babyyoda.y += 5
    if keysmovement[pygame.K_a] and babyyoda.x - 5 > 0:  # going left when u press A
        babyyoda.x -= 5
    if keysmovement[pygame.K_d] and babyyoda.x + 50 < 500:  # going right when u press D
        babyyoda.x += 5



# ---------------------------------Function to draw all the variables of the levels-------------------------------#
def drawscreen(babyyoda, darthvader, baby_yoda_bullets, BABY_YODA_HEALTH, DARTH_VADER_HEALTH, usertext, currenttime):
    PRINCIPALSCREEN1.fill((255, 255, 255))
    baby_yoda_health = fontofhp.render("LIFE:" + str(BABY_YODA_HEALTH), 1, (0, 0, 0))
    darth_vader_health = fontofhp.render("INVADER:" + str(DARTH_VADER_HEALTH), 1, (0, 0, 0))
    usertext = fontofhp.render("NAME:" + str(usertext), 1, (0, 0, 0))
    scoretext = fontofhp.render("SCORE:" + str(score), 1, (0, 0, 0))
    currenttime1 = fontofhp.render("TIME:" + str(currenttime), 1, (0, 0, 0)) # text of the variables on levels screen
    PRINCIPALSCREEN1.blit(baby_yoda_health, (10, 650))
    PRINCIPALSCREEN1.blit(darth_vader_health, (100, 650))
    PRINCIPALSCREEN1.blit(usertext, (230, 650))
    PRINCIPALSCREEN1.blit(scoretext, (20, 20))
    PRINCIPALSCREEN1.blit(currenttime1, (400, 20)) # it writes the text

    PRINCIPALSCREEN1.blit(BABY_YODA_SPACESHIP, (babyyoda.x, babyyoda.y))
    PRINCIPALSCREEN1.blit(DARTH_VADER, (darthvader.x, darthvader.y))
    for bullet in baby_yoda_bullets:
        pygame.draw.rect(PRINCIPALSCREEN1, (255, 0, 0), bullet)  # it draws the bullets

    pygame.display.update()


# ----------------------------------Function to make the bullets hit Darth Vader-------------------------------------#
def drawbullets(baby_yoda_bullets, darthvader):
    for bullet in baby_yoda_bullets:
        bullet.y -= 7
        if darthvader.x < bullet.x < darthvader.x + 50 and darthvader.y < bullet.y < darthvader.y + 50:
            # the bullet has to be be inside of darth vader
            global score
            score += 1  # when it hits darth vader it increase your score
            pygame.event.post(pygame.event.Event(DARTHVADERGOTHIT))
            baby_yoda_bullets.remove(bullet)
        elif bullet.y < 0:
            baby_yoda_bullets.remove(bullet)  # if the bullet it's out of the screen it get deleted

#def enemybullets(darth_vader_bullets, babyyoda, darthvader):
 #   for bullet in darth_vader_bullets:
  #      bullet.y += 7
   #     if darthvader.timer == 120:
    #        darthvader.timer = 0
     #       darthvader.shoot = True
      #      if babyyoda.x < bullet.x < babyyoda.x + 50 and babyyoda.y < bullet.y < babyyoda.y + 50:
       #         darthvader.shoot = True
        #        global BABY_YODA_HEALTH
         #       BABY_YODA_HEALTH += 1
          #      pygame.event.post(pygame.event.Event(YODAGOTHIT))
           #     darth_vader_bullets.remove(bullet)
            #elif bullet.y < 0:
            #    darth_vader_bullets.remove(bullet)
   #     elif darthvader.timer == 30 and darthvader.shoot == True:
     #       darthvader.readyshoot = True
    #    else:
      #      darthvader.timer += 1


# -----------------------Function to manipulate in a better way how the enemy moves-------------------------#
class darthvader1:  # class of the enemy
    def __init__(darthvader, x, y):
        darthvader.x = x
        darthvader.y = y
        darthvader.timer = 0
        darthvader.charge = False
        darthvader.attack = False
        darthvader.colliderect = False
        darthvader.readycharge = False
        darthvader.left = False
        darthvader.readyshoot = False
        darthvader.shoot = False
        darthvader.invading = True  # initial values


# --------------Function for the movement of Darth Vader in the first and third level--------------------#
def darthvadermoving(darthvader, DARTHVADERVELOCITY, ATTACKVELOCITY, babyyoda):
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


# -----------------------------------------Function for the level 1 screen---------------------------------------#
# GLOBAL SCORE
score = 0

def screenlevel1(usertext):
    # calls global values
    global score, BABY_YODA_HEALTH, DARTH_VADER_HEALTH
    score = 0

    babyyoda = pygame.Rect(225, 600, 50, 50) # rectangle to manipulate the spaceship
    darthvader = darthvader1(225, 100)  # to manipulate the enemy cause it can't be rect
    DARTH_VADER_HEALTH = 30  # HP of the enemy
    BABY_YODA_HEALTH = 50  # HP of the player
    baby_yoda_bullets = []  # bullets
    pygame.display.set_caption('Level 1') # title
    BABYYODAVELOCITY = 5 # velocity of the spaceship
    DARTHVADERVELOCITY = 2 # velocity of the enemy
    ATTACKVELOCITY = 12
    currenttime = 0
    timer = 0 # initial values
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

            if event.type == pygame.KEYDOWN: # Q to shoot
                if event.key == pygame.K_q:
                    bullet = pygame.Rect(babyyoda.x + 25, babyyoda.y + 25, 5, 10)
                    baby_yoda_bullets.append(bullet)

            if event.type == DARTHVADERGOTHIT: # if the enemy gets damage it decreases his life
                DARTH_VADER_HEALTH -=1

            if event.type == YODAGOTHIT:  # when baby yoda gets damage it decreases his life by 10 pts
                BABY_YODA_HEALTH -= 10

        if DARTH_VADER_HEALTH <= 0: # if you finish the level in lessthan 30 seconds you get a bonus of 20 pts
            if currenttime <= 30:
                score += 20
            if BABY_YODA_HEALTH == 50: # if u don't get damage you get a bonus of 10 pts
                score += 10
            screenlevel2(usertext, score)
            flag = 0

        if BABY_YODA_HEALTH <= 0: # if u die it takes you to the main screen
            mainscreen()
            flag = 0

        darthvadermoving(darthvader, ATTACKVELOCITY, DARTHVADERVELOCITY, babyyoda)
        attack(darthvader, ATTACKVELOCITY) # functions to move and to charge the enemy


        if timer == 60: # timer
            timer = 0
            currenttime += 1
        else:
            timer += 1
        keysmovement = pygame.key.get_pressed()
        baby_yoda_movement(keysmovement, babyyoda)
        drawscreen(babyyoda, darthvader, baby_yoda_bullets, BABY_YODA_HEALTH, DARTH_VADER_HEALTH, usertext, currenttime)
        drawbullets(baby_yoda_bullets, darthvader)
        pygame.display.update()
        clock.tick(60) # recursivity of the functions every 60 FPS


# ----------------------------------------Function for the level 2 function--------------------------------------------#
#GLOBAL SCORE
score = 0

def screenlevel2(usertext, score2 = 0):

    global score
    score = 0
    babyyoda = pygame.Rect(225, 600, 50, 50) # rectangle to manipulate the spaceship
    darthvader = darthvader1(225, 100)  # to manipulate the enemy cause it can't be rect
    DARTH_VADER_HEALTH = 50  # HP of the enemy
    BABY_YODA_HEALTH = 50  # HP of the player
    baby_yoda_bullets = []  # bullets
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    bullet = pygame.Rect(babyyoda.x + 25, babyyoda.y + 25, 5, 10)
                    baby_yoda_bullets.append(bullet)

            if event.type == DARTHVADERGOTHIT:  # when the enemy gets hit it - to the enemy's life
                DARTH_VADER_HEALTH -=1

            if event.type == YODAGOTHIT:  # when the player got hit it - to the player's HP
                BABY_YODA_HEALTH -= 10

            if DARTH_VADER_HEALTH <= 0:
                if currenttime <= 30:
                    score += 20  # if you finish before 30s has passed you get a  +20 pts bonus
                if BABY_YODA_HEALTH == 50:
                    score += 10  # if you finish without getting any damage you get a  +20 pts bonus
                screenlevel3(usertext, score)
                flag = 0

            if BABY_YODA_HEALTH <= 0:  # if you die it goes back to the primcipal screen
                mainscreen()
                flag = 0

        if timer == 60:  # function of the timer
            timer = 0
            currenttime += 1
        else:
            timer += 1

        keysmovement = pygame.key.get_pressed()
        baby_yoda_movement(keysmovement, babyyoda)
        drawscreen(babyyoda, darthvader, baby_yoda_bullets, BABY_YODA_HEALTH, DARTH_VADER_HEALTH, usertext, currenttime)
        drawbullets(baby_yoda_bullets, darthvader)
        pygame.display.update()
        clock.tick(60) # all of the functions called are in the while so they do the recursivity

# --------------------------------------Function for the level 3 screen----------------------------------------------#
#GLOBAL SCORE
score = 0

def screenlevel3(usertext, score3):

    global score, BABY_YODA_HEALTH, DARTH_VADER_HEALTH
    score = 0

    babyyoda = pygame.Rect(225, 600, 50, 50) # rectangle to manipulate the spaceship
    darthvader = darthvader1(225, 100)  # to manipulate the enemy cause it can't be rect
    DARTH_VADER_HEALTH = 40  # HP of the enemy
    BABY_YODA_HEALTH = 50  # HP of the player
    baby_yoda_bullets = []  # bullets
    darth_vader_bullets = []
    pygame.display.set_caption('Level 3') # title
    DARTHVADERVELOCITY = 2  # velocity of the enemy
    ATTACKVELOCITY = 12  # velocity of the player
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
                    mainscreen()
                    pygame.display.set_caption('Operation Moon light')

            if event.type == pygame.KEYDOWN: # to shoot the bullets when you press Q
                if event.key == pygame.K_q:
                    bullet = pygame.Rect(babyyoda.x + 25, babyyoda.y + 25, 5, 10)
                    baby_yoda_bullets.append(bullet)

            if event.type == DARTHVADERGOTHIT: # when the enemy gets hit it - to the enemy's life
                DARTH_VADER_HEALTH -=1

            if event.type == YODAGOTHIT:  # when the player got hit it - to the player's HP
                BABY_YODA_HEALTH -= 10

            if DARTH_VADER_HEALTH <= 0:
                if currenttime <= 30:
                    score += 20  # if you finish before 30s has passed you get a  +20 pts bonus
                if BABY_YODA_HEALTH == 50:
                    score += 10  # if you finish without getting any damage you get a  +20 pts bonus
                screenleaderboard(usertext, score)
                flag = 0

            if BABY_YODA_HEALTH <= 0:  # if you die it goes back to the primcipal screen
                mainscreen()
                flag = 0

        darthvadermoving(darthvader, ATTACKVELOCITY, DARTHVADERVELOCITY, babyyoda)  # function so Darth Vdaer moves
        attack(darthvader, ATTACKVELOCITY)  # function to charge in direction to baby yoda
#        enemybullets(darth_vader_bullets, babyyoda, darthvader)

        if timer == 60:  # function of the timer
            timer = 0
            currenttime += 1
        else:
            timer += 1

        keysmovement = pygame.key.get_pressed()
        baby_yoda_movement(keysmovement, babyyoda)
        drawscreen(babyyoda, darthvader, baby_yoda_bullets, BABY_YODA_HEALTH, DARTH_VADER_HEALTH, usertext, currenttime)
        drawbullets(baby_yoda_bullets, darthvader)
        pygame.display.update()
        clock.tick(60)  # all of the functions called are in the while so they do the recursivity


# ------------------------------------------Text for the instructions window-----------------------------------------#
fontoftitle = pygame.font.Font(None, 40)
fontofsubtitle = pygame.font.Font(None, 30)
textoftitle2 = fontoftitle.render("Instructions", 0, (255, 255, 255))
textofspam = fontofsubtitle.render("Select:Information to know about the developer", 0, (255, 255, 255))
textoflevel = fontofsubtitle.render("Select the level you want to play", 0, (255, 255, 255))
textofwasd = fontofsubtitle.render("Move with w,a,s,d to move", 0, (255, 255, 255))
textofmovement = fontofsubtitle.render("front,left,back and right", 0, (255, 255, 255))
textofshoot = fontofsubtitle.render("to shoot press e", 0, (255, 255, 255))
textofasap = fontofsubtitle.render("kill the boss asap and try to not get damage", 0, (255, 255, 255))
textofscorentime = fontofsubtitle.render("your score and the time will show in the screen", 0, (255, 255, 255))
textoflastline = fontofsubtitle.render("while you're playing", 0, (255, 255, 255))

#-----------------------------------------Function for the istructions screen------------------------------------------#
def screeninstructions():
    pygame.display.set_caption('Instructions') # title
    running = True
    while running:
        PRINCIPALSCREEN1.fill((0, 0, 0)) # to fill the screen

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # to go to the last screen
                    running = False
                    pygame.display.set_caption('Operation Moon light')

# It writes the text on a posicion x,y
        PRINCIPALSCREEN1.blit(textoftitle2, (180, 150))
        PRINCIPALSCREEN1.blit(textofspam, (20, 200))
        PRINCIPALSCREEN1.blit(textoflevel, (110, 250))
        PRINCIPALSCREEN1.blit(textofwasd, (140, 300))
        PRINCIPALSCREEN1.blit(textofmovement, (150, 350))
        PRINCIPALSCREEN1.blit(textofshoot, (190, 400))
        PRINCIPALSCREEN1.blit(textofasap, (40, 450))
        PRINCIPALSCREEN1.blit(textofscorentime, (20, 500))
        PRINCIPALSCREEN1.blit(textoflastline, (160, 550))

        pygame.display.update()
        clock.tick(60)


# ------------------------------------------Text for the about window-----------------------------------------#
# Fonts for the about screen's text
fontoftitle = pygame.font.Font(None, 40)
fontofsubtitle = pygame.font.Font(None, 30)
textoftitle1 = fontoftitle.render("About", 0, (255, 255, 255))
textofstudent = fontofsubtitle.render("Student: Abraham Venegas Mayorga", 0, (255, 255, 255))
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
    pygame.display.set_caption('About') # title of the window
    running = True
    while running:
        PRINCIPALSCREEN1.fill((0, 0, 0)) # to fill the screen

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # to go to the last screen
                    running = False
                    pygame.display.set_caption('Operation Moon light')

# It writes the text on the posicion x, y
        PRINCIPALSCREEN1.blit(textoftitle1, (210, 150))
        PRINCIPALSCREEN1.blit(textofversion, (80, 200))
        PRINCIPALSCREEN1.blit(textofstudent, (80, 250))
        PRINCIPALSCREEN1.blit(textofteacher, (110, 300))
        PRINCIPALSCREEN1.blit(textofce, (150, 350))
        PRINCIPALSCREEN1.blit(textofcourse, (140, 400))
        PRINCIPALSCREEN1.blit(textofcr, (140, 450))
        PRINCIPALSCREEN1.blit(textofGroup, (210, 500))
        PRINCIPALSCREEN1.blit(textofU, (225, 550))
        PRINCIPALSCREEN1.blit(textofyear, (225, 600))

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