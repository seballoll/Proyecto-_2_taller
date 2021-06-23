# General Setup: we call the librarie to start programming the game
import pygame, sys
import random  # so we can manipulate the random number that the enemy throws
from pygame.locals import *
import vlc  # lib to use sounds in the game

# ------------------------------------------- General settings ---------------------------------------#
pygame.init()
clock = pygame.time.Clock()  # function for the timer
timer = 0  # inital value
PRINCIPALSCREEN1 = pygame.display.set_mode([700, 700])  # to pop up the screen
pygame.display.set_caption('Ninja Dash')  # title
icon1 = pygame.image.load("ninja .png")  # icon
pygame.display.set_icon(icon1)  # to display the icon of  the ninja


# -------------------------------------------Text for the principal window---------------------------------------#
# Fonts of the text
fontoftitle = pygame.font.Font(None, 40)
fontofsubtitle = pygame.font.Font(None, 30)
fontofhp = pygame.font.Font(None, 30)

# Texts
#textoftitle = fontoftitle.render("立竜の物語", 0, (255, 255, 255))
# the title says "Ritsuryu no monogatari" which means "La historia del dragón ascendente"
textofsubtitle = fontofsubtitle.render("Entry your name", 0, (255, 255, 255))
textofindication = fontofsubtitle.render("(Write a short name)", 0, (255, 255, 255))
textoflvl1 = fontofsubtitle.render("Level1", 0, (0, 0, 0))
textoflvl2 = fontofsubtitle.render("Level2", 0, (0, 0, 0))
textoflvl3 = fontofsubtitle.render("Level3", 0, (0, 0, 0))
textofinstructions = fontofsubtitle.render("Instructions", 0, (0, 0, 0))
textofaboutinfo = fontofsubtitle.render("About", 0, (0, 0, 0))
textofleaderboard = fontofsubtitle.render("Leaderboard", 0, (0, 0, 0))


# ------------------------------------- Class for the background's photos ------------------------------------------#


class backgroun_image:  # we define the function
    def __init__(self,level):
        self.level = level
        self.bg1 = pygame.image.load("background images/bamboo forest.jpg")
        # and put the photos in each screen in this case level 1
        self.bg2 = pygame.image.load("background images/sakura forest.jpg")  # for the level 2
        self.bg3 = pygame.image.load("background images/torii.jpg")  # for the level 3
        self.about = pygame.image.load("background images/torii.jpg")  # for the about's screen
        self.intructions = pygame.image.load("background images/Japanese-garden.jpg")   # for the instructions's screen
        self.leaderboards = pygame.image.load("background images/void.jpg")  # for the leaderboard's screen
    def choose_level(self):  # we define a function to give a background photo for each level
        if self.level == 1:
            return self.bg1
        elif self.level == 2:
            return  self.bg2
        elif self.level == 3:
            return self.bg3


# ------------------------------------------ sound -----------------------------------------------#

clinck = pygame.mixer.music.load("sounds/metallic-clink.wav")  # sound for the shurikens
music4 = vlc.MediaPlayer("sounds/Using What You Got.mp3")  # mainscreen's music


# ------------------------------------------ Function of the principal screen -----------------------------------------#

# initial values
clickbutton = False
active = False

# GLOBAL SCORE
score = 0


def play_bgm():  # function to play the music of the mainscreen
    music4.play()
    music4.audio_set_volume(50)


def mainscreen():
    # initial values
    clickbutton = False  # variable to select the other screens
    play_bgm()  # for the music
    active = False  # variable to validate when u click
    usertext = ''   # variable to save the name
    bg1 = pygame.image.load("background images/dojo.jpg")  # mainscreen's background photo

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
                music4.stop()  # to stop the mainscreen's music i u go to other screen in each screen
                screenlevel1(usertext,score)
        if level2.collidepoint((mx, my)):
            if clickbutton:
                music4.stop()
                screenlevel2(usertext,score)
        if level3.collidepoint((mx, my)):
            if clickbutton:
                music4.stop()
                screenlevel3(usertext, score)
        if instructions.collidepoint((mx, my)):
            if clickbutton:
                music4.stop()
                screeninstructions()
        if about.collidepoint((mx, my)):
            if clickbutton:
                music4.stop()
                aboutscreen()
        if leaderboard.collidepoint((mx, my)):
            if clickbutton:
                music4.stop()
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
        #PRINCIPALSCREEN1.blit(textoftitle, (125, 50))  # it writes the titles of the rectangles
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


# --------------------------------------------------- GAME CONFIG---------------------------------------------------#

# Variables to manipulate in the levels
NINJAGOTHIT = pygame.USEREVENT  # event when the ninja get damage
NINJA_HEALTH = 3  # Ninja's hp


# ----------------------------------------------- Ninja Class    -------------------------------------------------#


class Ninja:

        Ninja_image = pygame.image.load("ninja .png")  # the photo of the ninja
        Ninja = pygame.transform.scale(Ninja_image, (50, 50))  # to adjust it to the scale of the rectangle
        speed = [1,0]  # speed of the ninja


# ----------------------------------------------- Shuriken Class -------------------------------------------------#


class Shuriken:

    def __init__(self,image):
        self.Shuriken_image = image  # photo of the shuriken
        self.shurickenrect = self.Shuriken_image.get_rect()
        self.speed = [8, 8]  # speed of the shuriken
    def bounce_positive(self):
        return random.randint(0, 8)
    def bounce_negative(self):
        return random.randint(-8, 0)
    def bounce_random(self):  # the function pics a random number so it changes the direction
        return random.randint(-8, 8)
    def get_image(self):  # photo of the shuriken
        image = self.Shuriken_image
        return image
    def get_recta(self):
        rect = self.shurickenrect
        return rect
    def get_speed(self):  # function for the speed
        speed = self.speed
        return speed
    def set_move(self):
        self.shurickenrect = self.shurickenrect.move(self.speed)


amount_shuriken = []  # variable to pick a certain amount of shurikens to show on the screen

# --------------------------------------- Function to create a lot of shurikens ----------------------------#


def create_shurikens(level):  # function to pick the amount in each level
    global amount_shuriken
    if level == 1:  # for level 1
        for x in range(0, 5):  # 5 shurikens in this levels
            x = Shuriken(pygame.image.load("shuriken.png"))  # each one with the shuriken's photo
            amount_shuriken += [x]  # it puts every shuriken till it print all the 5 shurikens
    elif level == 2:  # for level 1
        for x in range(0, 7):  # 7 shurikens in this levels
            x = Shuriken(pygame.image.load("shuriken.png"))  # each one with the shuriken's photo
            amount_shuriken += [x]  # it puts every shuriken till it print all the 7 shurikens
    else:
        for x in range(0, 10):   # for level 1 and 10 shurikens in this levels
            x = Shuriken(pygame.image.load("shuriken.png"))  # each one with the shuriken's photo
            amount_shuriken += [x]  # it puts every shuriken till it print all the 10 shurikens


music1 = vlc.MediaPlayer("sounds/Fighting Without Honor.mp3")  # music for the first level
music2 = vlc.MediaPlayer("sounds/Hiding in the Shadows.mp3")  # music for the second level
music3 = vlc.MediaPlayer("sounds/RoBomb.mp3")  # music for the third level


def play_music(level):  # function to play the music in each level
    if level == 1:  # in the first level
        music1.play()  # to play the song
        music1.audio_set_volume(50)  # to regulate the volume
    elif level == 2:  # in the second level
        music2.play()  # to play the song
        music2.audio_set_volume(50)  # to regulate the volume
    else:  # in the third level
        music3.play()  # to play the song
        music3.audio_set_volume(50)  # to regulate the volume


# -----------------------------------Function for the movement of the ninja---------------------------------------#


def ninja_movement(keysmovement, ninja):
    if keysmovement[pygame.K_w] and ninja.y - 5 > 0:  # going up when u press W
        ninja.y -= 5
    if keysmovement[pygame.K_s] and ninja.y + 5 + 50 < 700:  # going down when u press D
        ninja.y += 5
    if keysmovement[pygame.K_a] and ninja.x - 5 > 0:  # going left when u press A
        ninja.x -= 5
    if keysmovement[pygame.K_d] and ninja.x + 50 < 700:  # going right when u press D
        ninja.x += 5


# ---------------------------------Function to draw all the variables of the levels-------------------------------#


do_shuriken = True  # variable to create the shurikens


def drawscreen(ninja, NINJA_HEALTH, usertext, currenttime, level):
    background_image = backgroun_image(level)  # background photo
    PRINCIPALSCREEN1.blit(background_image.choose_level(), (0, 0))
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


    global do_shuriken, amount_shuriken
    while  do_shuriken:
        create_shurikens(level)
        do_shuriken = False


    for x in amount_shuriken:
        x.set_move()


    for x in amount_shuriken:
        PRINCIPALSCREEN1.blit(x.get_image(),(x.get_recta()))



    pygame.display.update()


# -----------------------------------------Function for the level 1 screen---------------------------------------#


def screenlevel1(usertext,score1):
    # calls global values
    global  NINJA_HEALTH, Ninja_image, do_shuriken, score
    do_shuriken = True
    score = 0  # score of the level
    ninja = pygame.Rect(225, 600, 50, 50)  # rectangle to manipulate the ninja
    play_music(1)  # to play the first song
    NINJA_HEALTH = 3  # HP of the player
    pygame.display.set_caption('Level 1')  # title
    currenttime = 0  # for the timer in the screen
    timer = 0  # initial values
    running = True
    while running:
        PRINCIPALSCREEN1.fill((0, 0, 0))

        for event in pygame.event.get():
            global amount_shuriken
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # to go to the main screen with ESCAPE
                if event.key == K_ESCAPE:
                    amount_shuriken = []
                    music1.stop()
                    running = mainscreen()
                    pygame.display.set_caption('Ninja dash')  # puts the title

        if NINJA_HEALTH <= 0:  # if u die it takes you to the main screen
            format = usertext + "/" + str(score)
            info = "[" + format + "]"  # and gives you your score
            save_score(info)
            music1.stop()
            mainscreen()
            flag = 0


        for x in amount_shuriken:
            rect = x.get_recta()

            # it changes the speed of the  shuriken
            if rect.left <= 0:  # if it's on the left border it changes the direction to the right
                x.speed = [Shuriken.bounce_positive(Shuriken), Shuriken.bounce_random(Shuriken)]
                pygame.mixer.music.play(0)  # if it hits the border, plays the sound
            if rect.right >= 750:  # if it's on the right border it changes the direction to the left
                pygame.mixer.music.play(0)
                x.speed = [Shuriken.bounce_negative(Shuriken), Shuriken.bounce_random(Shuriken)]

            if rect.top <= 0:   # if it's on the top border it changes the direction to the bottom
                pygame.mixer.music.play(0)
                x.speed = [Shuriken.bounce_random(Shuriken), Shuriken.bounce_positive(Shuriken)]

            if rect.bottom >= 700:   # if it's on the bottom border it changes the direction to the top
                pygame.mixer.music.play(0)
                x.speed = [Shuriken.bounce_random(Shuriken), Shuriken.bounce_negative(Shuriken)]
            if ninja.left <= rect.right <= ninja.right and ninja.left <= rect.left <= ninja.right: # for a shuriken hitting the ninja
                del x
                NINJA_HEALTH -=1


            if timer == 60:  # timer
                timer = 0
                currenttime += 1
                score += 1  # it increases the score for every second
            else:
                timer += 1

            if currenttime == 60:  # if the timer is on 60s
                format = usertext + "/" + str(score)
                info = "[" + format + "]"
                save_score(info)  # it saves the score
                music1.stop()  # stop the music
                amount_shuriken = []  # and put the shurikens on 0
                running = screenlevel2(usertext,score)  # and starts running the second level

        keysmovement = pygame.key.get_pressed()
        ninja_movement(keysmovement, ninja)  # to move the ninja
        drawscreen(ninja, NINJA_HEALTH, usertext, currenttime, 1)
        clock.tick(60)  # recursivity of the functions every 60 FPS
        pygame.display.update()


# --------------------------------------Function for the level 2 function------------------------------------------#


def screenlevel2(usertext, score2 = 0):

    global  NINJA_HEALTH, do_shuriken, amount_shuriken, score
    do_shuriken = True
    score = 0
    ninja = pygame.Rect(225, 600, 50, 50)  # rectangle to manipulate the ninja
    play_music(2)  # plays the second song
    NINJA_HEALTH = 3  # HP of the player (ninja)
    pygame.display.set_caption('Level 2')  # title
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
                if event.key == K_ESCAPE:  # to go to the main screen if u press ESCAPE
                    amount_shuriken = []
                    music2.stop()  # it stops the music
                    running = mainscreen()
                    pygame.display.set_caption('ninja dash')


            if NINJA_HEALTH <= 0:  # if you die it goes back to the principal screen
                format = usertext + "/" + str(score)
                info = "[" + format + "]"
                save_score(info)
                music2.stop()
                mainscreen()
                flag = 0
        for x in amount_shuriken:
            rect = x.get_recta()
            if x.get_recta().left <= 0:
                x.speed = [Shuriken.bounce_positive(Shuriken), Shuriken.bounce_random(Shuriken)]
                pygame.mixer.music.play(0)
            if x.get_recta().right >= 750:
                pygame.mixer.music.play(0)
                x.speed = [Shuriken.bounce_negative(Shuriken), Shuriken.bounce_random(Shuriken)]

            if x.get_recta().top <= 0:
                pygame.mixer.music.play(0)
                x.speed = [Shuriken.bounce_random(Shuriken), Shuriken.bounce_positive(Shuriken)]

            if x.get_recta().bottom >= 700:
                pygame.mixer.music.play(0)
                x.speed = [Shuriken.bounce_random(Shuriken), Shuriken.bounce_negative(Shuriken)]
            if ninja.left <= rect.right <= ninja.right and ninja.left <= rect.left <= ninja.right:
                del x
                NINJA_HEALTH -=1

            if timer == 60: # timer
                timer = 0
                currenttime += 1
                score += 3  # it increases the score with 3 pts every second
            else:
                timer += 1

            if currenttime == 60:
                format = usertext + "/" + str(score)
                info = "[" + format + "]"
                save_score(info)
                music2.stop()
                amount_shuriken = []
                running = screenlevel3(usertext,score)


        keysmovement = pygame.key.get_pressed()
        ninja_movement(keysmovement, ninja)
        drawscreen(ninja, NINJA_HEALTH, usertext, currenttime, 2)
        pygame.display.update()
        clock.tick(60)  # all of the functions called are in the while so they do the recursivity

# --------------------------------------Function for the level 3 screen----------------------------------------------#
# GLOBAL SCORE



def screenlevel3(usertext, score3):
    global score, NINJA_HEALTH, do_shuriken, amount_shuriken
    score = 0
    ninja = pygame.Rect(225, 600, 50, 50)  # rectangle to manipulate the ninja
    NINJA_HEALTH = 3  # HP of the player
    do_shuriken = True
    play_music(3)  # it plays the third song
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
                    amount_shuriken = []
                    music3.stop()
                    running = mainscreen()
                    mainscreen()
                    pygame.display.set_caption('ninja dash')


            if NINJA_HEALTH <= 0:  # if you die it goes back to the principal screen
                format = usertext + "/" + str(score)
                info = "[" + format + "]"
                save_score(info)
                music3.stop()
                mainscreen()
                flag = 0

        for x in amount_shuriken:
            rect = x.get_recta()
            if x.get_recta().left <= 0:
                x.speed = [Shuriken.bounce_positive(Shuriken), Shuriken.bounce_random(Shuriken)]
                pygame.mixer.music.play(0)
            if x.get_recta().right >= 750:
                pygame.mixer.music.play(0)
                x.speed = [Shuriken.bounce_negative(Shuriken), Shuriken.bounce_random(Shuriken)]

            if x.get_recta().top <= 0:
                pygame.mixer.music.play(0)
                x.speed = [Shuriken.bounce_random(Shuriken), Shuriken.bounce_positive(Shuriken)]

            if x.get_recta().bottom >= 700:
                pygame.mixer.music.play(0)
                x.speed = [Shuriken.bounce_random(Shuriken), Shuriken.bounce_negative(Shuriken)]
            if ninja.left <= rect.right <= ninja.right and ninja.left <= rect.left <= ninja.right:
                del x
                NINJA_HEALTH -= 1

            if timer == 60:  # timer
                timer = 0
                currenttime += 1
                score += 5
            else:
                timer += 1

        if currenttime == 60:  # if the timer equals to 60s
            format = usertext + "/" + str(score)
            info ="[" +format+ "]"
            save_score(info)  # it saves teh score
            music3.stop()  # and stops the music
            running = mainscreen()  # adn takes you to the mainscreen


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
                    running = mainscreen()
                    pygame.display.set_caption('Operation Moon light')

        bgi = pygame.image.load("background images/Japanese-garden.jpg")
        PRINCIPALSCREEN1.blit(bgi,(0,0))

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
    bg = pygame.image.load("background images/ninja style.jpg")
    while running:
        PRINCIPALSCREEN1.fill((0, 0, 0))  # to fill the screen

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # to go to the last screen
                    running = mainscreen()
                    pygame.display.set_caption('ninja dash')

# It writes the text on the posicion x, y
        PRINCIPALSCREEN1.blit(bg, (0, 0))
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
def format_str(top7):
    text = ""
    for x in top7:
        text += x
    return text

def screenleaderboard(usertext, score):
    pygame.display.set_caption('Leaderboard')  # to write the Title
    top7 = show_score()[:7]
    top7string = format_str(top7)
    print(top7)
    print(top7string)
    text = fontofsubtitle.render(top7string,0,(0,0,0))
    running = True
    while running:
        PRINCIPALSCREEN1.fill((0, 0, 0))  # to fill with white the background

        for event in pygame.event.get():
            if event.type == QUIT:  # this quits the game
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # this function takes you to the last screen when u hit space
                if event.key == K_ESCAPE:
                    running = mainscreen()
                    pygame.display.set_caption('Ninja dash')

        bgi = pygame.image.load("background images/void.jpg")
        PRINCIPALSCREEN1.blit(bgi, (0, 0))
        PRINCIPALSCREEN1.blit(text,(70,65))
        pygame.display.update()  # updates every 60 FPS
        clock.tick(60)


def save_score(info):  # function to save the score
    with open("score.txt", "a") as f:
        f.write(info+"\n")


def show_score():  # function to show the score on the leaderboard
    with open("score.txt", "r") as f:
        scores = f.read()
        i = 0
        start = 0
        end = 0  # initial values
        list_scores = []  # on the beginning there's no score cause no one has ever played
        for x in scores:
            if x == "[":
                start = i
                i += 1
            elif x == "]":
                end = i
                list_scores += [scores[start:end+1]]
                i += 1
            else:
                i += 1
        return make_number(list_scores)


def make_number(lista):
      index = 0
      number_list = []
      dictionary = { }
      while index != len(lista):
          number_start = 0

          for x in lista[index]:
              if x == "/":

                  number_list += [int(lista[index][number_start+1:-1])]
                  dictionary.update({int(lista[index][number_start+1:-1]):index})
                  break
              else:
                  number_start += 1
          index += 1
      return give_order(quicksort(number_list),dictionary,lista)


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[-1]
        lista = lista[:-1]
    menor = []
    mayor = []
    for x in lista:
        if x > pivot:
            mayor += [x]
        else:
            menor += [x]
    return quicksort(mayor) + [pivot] + quicksort(menor)


def give_order(lista, dictionary, list):
    final_format = []
    for x in lista:
        if x in dictionary:
            final_format += [list[dictionary[x]]]
    return final_format


mainscreen()
