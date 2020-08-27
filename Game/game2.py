import pygame


pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue=(0,0,255)
color = (123,231,213)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20]=red

pygame.draw.line(gameDisplay,blue,(100,200),(100,300 ),7)

pygame.draw.rect(gameDisplay,green,(400,400,500,25))

pygame.draw.circle(gameDisplay,color,(300,300),56)

pygame.draw.polygon(gameDisplay,green,((25,75),(76,125),(250,375),(400,25)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()