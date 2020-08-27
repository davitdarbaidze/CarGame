
import time as t
import random as rnd
import pygame

pygame.init()

crash_sound = pygame.mixer.Sound("C:/Users/User/Desktop/Game/Game/crash2.wav")
pygame.mixer.music.load("C:/Users/User/Desktop/Game/Game/music.mp3")


display_width = 800
display_height  = 600
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

pause = True

global thing_starx
carImg = pygame.image.load("C:/Users/User/Desktop/Game/Game/car.png")
pygame.display.set_icon(carImg)
#cakeImg= pygame.image.load("C:/Users/user/Desktop/Games/cake.jpg")
car_width = 100

gameDisplay = pygame.display.set_mode((display_width,display_height ))
pygame.display.set_caption("best game ever")

clock = pygame.time.Clock()


def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("dodged: " + str(count),True,black)
    gameDisplay.blit(text,(0,0))
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])


class MoreRectangles:
    def __init__(self,thing_startx,thing_starty,thing_speed,thing_width,thing_height,thing_color):
        self.thing_startx = thing_startx
        self.thing_starty = thing_starty
        self.thing_speed = thing_speed        
        self.thing_width = thing_width
        self.thing_height = thing_height
        self.thing_color = thing_color

    def rectangles(self):        
        things(self.thing_startx,self.thing_starty,self.thing_width,self.thing_height,self.thing_color)

def car(x,y):    
    gameDisplay.blit(carImg,(x,y))
def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2,display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    t.sleep(2)
    game_loop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display('you crashed')

def button(msg,x,y,w,h,inactiveColor,ativeColor,action=None):
    mouse = pygame.mouse.get_pos()
    mousepress = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ativeColor,(x,y,w,h))
        if mousepress[0] == True and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,inactiveColor,(x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf,textRect = text_objects(msg, smallText)    
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf,textRect)

def unPause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def pauseMenu():
    pygame.mixer.music.pause()
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Game Paused",largeText)
    TextRect.center = ((display_width/2,display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        button("Continue",150,450,100,50,green,bright_green,unPause)
        button("Quit",550,450,100,50,red,bright_red,quitGame)
        pygame.display.update()
    
     
def quitGame():
    pygame.mixer.stop()
    pygame.quit()
    quit()

def game_intro():
    intro = True
    

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Racing game",largeText)
        TextRect.center = ((display_width/2,display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        

        button("Go",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitGame)

        

        '''
        mouse = pygame.mouse.get_pos()
        mousepress = pygame.mouse.get_pressed()
        

        if(150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450):
            pygame.draw.rect(gameDisplay,bright_green,(150,450,100,50))
            if mousepress[0] == True:
                game_loop()
        else:
            pygame.draw.rect(gameDisplay,green,(150,450,100,50))
        


        if(550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450):
            pygame.draw.rect(gameDisplay,bright_red,(550,450,100,50))
            if mousepress[0]== True:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay,red,(550,450,100,50))


        startText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf1, TextRect1 = text_objects("start",startText,red)
        TextRect1.center = ((200,475))
        gameDisplay.blit(TextSurf1,TextRect1)
        quitText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf2, TextRect2 = text_objects("Quit",quitText,black)
        TextRect2.center = ((600,475))
        gameDisplay.blit(TextSurf2,TextRect2)

        '''


        pygame.display.update()
        #print(clock)
        clock.tick(15)
        



def game_loop():
    pygame.mixer.music.play(-1)
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0


    r1 = MoreRectangles(rnd.randrange(0,display_width),-600,2,100,100,black)

    
    r2 = MoreRectangles(rnd.randrange(0,display_width),-600,2,100,100,red)
    dodged = 0
    
    
    
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key== pygame.K_RIGHT:
                    x_change = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    pauseMenu()
                    


        x += x_change
        gameDisplay.fill(white)   


        #things(thingx,thingy,thingw,thingh,color)
        
        #things(thing_startx,thing_starty,thing_width,thing_height,black)
        
        
                 
        r1.rectangles()
        r2.rectangles()
        r1.thing_starty += r1.thing_speed
        #print(r1.thing_starty)
        
        car(x,y)
        things_dodged(dodged)

        if(x > display_width-car_width or x < 0):
            crash()
            gameExit = True
        if r1.thing_starty > display_height or r1.thing_startx > display_width-100:
            #print(thing_starty)
            r1.thing_starty = 0 - r1.thing_height
            r1.thing_startx = display_width-100
            
            r1.thing_startx = rnd.randrange(0,display_width)
            
            dodged +=1
            r1.thing_speed +=1
            r1.thing_width += (dodged * 1.2)      

        if y < (r1.thing_starty + r1.thing_height):
            #print('step 1')
            if x > r1.thing_startx and x < r1.thing_startx + r1.thing_width or x+ car_width > r1.thing_startx and x+ car_width < r1.thing_startx + r1.thing_width:
                #print('x crossover')
                crash()
                gameExit = True
        #r2        
        r2.thing_starty += r2.thing_speed
        #print(r2.thing_starty)
        
        car(x,y)
        things_dodged(dodged)


        if r2.thing_starty > display_height or r2.thing_startx > display_width-100:
            #print(thing_starty)
            r2.thing_starty = 0 - r2.thing_height
            r2.thing_startx = display_width-100
            
            r2.thing_startx = rnd.randrange(0,display_width)
            
            dodged +=1
            r2.thing_speed +=1
            r2.thing_width += (dodged * 1.2)      

        if y < (r2.thing_starty + r2.thing_height):
           # print('step 1')
            if x > r2.thing_startx and x < r2.thing_startx + r2.thing_width or x+ car_width > r2.thing_startx and x+ car_width < r2.thing_startx + r2.thing_width:
                #print('x crossover')
                crash()
                gameExit = True                   
        pygame.display.update()
        clock.tick(90)

game_intro()
game_loop()
pygame.quit()
quit()