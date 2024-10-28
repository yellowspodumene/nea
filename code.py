import pygame, sys

from pygame.locals import *

class Wall(object):

    def __init__(self, colour, x, y):

        self.width = 20

        self.height = 20

        self.x = x

        self.y = y

        self.colour = colour

        self.image = makePygameRectangle(self.colour, self.x,self.y,self.width,self.height)

        self.blank = False

    def render(self):

        if not self.blank:

            pygame.draw.rect(mySurface, self.colour, self.image)

 

width = 1000

height = 1000

my_caption = 'Menu'


BLACK = (0,0,0,255)
RED = (227, 93, 93)
WHITE= (252,252,252)
BLUE = (61, 136, 161)
PURPLE = (228, 143, 247)


def initialise(windowWidth, windowHeight, windowName, windowColour):
 
 

    pygame.init()

    mySurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)

    pygame.display.set_caption(windowName)

    mySurface.fill(windowColour)

 

    return mySurface

 
def makePygameRectangle(colour, xPos, yPos, width, height):
    myRect = pygame.Rect(xPos,yPos, width, height)
    pygame.draw.rect(mySurface, colour, myRect)

    return myRect
 
mySurface = initialise(width, height, my_caption, RED)

while True:

   
    menu = pygame.draw.rect(mySurface, WHITE, (370,150,250,150))
    menu1 = pygame.font.SysFont('calibri', 60)
    menubox = menu1.render('Menu', True, BLACK)
    mySurface.blit(menubox, (425, 200))
   
    easy = pygame.draw.rect(mySurface, PURPLE, (150,500,150,100))
    easy1 = pygame.font.SysFont('calibri', 40)
    easybox = easy1.render('Easy', True, BLACK)
    mySurface.blit(easybox, (185, 520))
   
    medium = pygame.draw.rect(mySurface, PURPLE, (430,500,150,100))
    medium1 = pygame.font.SysFont('calibri', 40)
    mediumbox = medium1.render('Medium', True, BLACK)
    mySurface.blit(mediumbox, (435, 520))
   
    hard = pygame.draw.rect(mySurface, PURPLE, (730,500,150,100))
    hard1 = pygame.font.SysFont('calibri', 40)
    hardbox = hard1.render('Hard', True, BLACK)
    mySurface.blit(hardbox, (765, 520))
   
    tutorial = pygame.draw.rect(mySurface, BLUE, (410,320,180,100))
    tutorial1 = pygame.font.SysFont('calibri', 40)
    tutorialbox = tutorial1.render('Tutorial', True, BLACK)
    mySurface.blit(tutorialbox, (440, 350))
   

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()
 

    pygame.display.update()
