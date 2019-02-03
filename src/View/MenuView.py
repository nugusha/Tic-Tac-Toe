import pygame
import sys
from TicTacToe import TicTacToe

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
MENU_COLOR = (234, 255, 34)

class MenuView:
    def __init__(self,GRID_SIZE,players):
        pygame.init()
        self.GRIDSIZE = GRID_SIZE
        self.SQUARESIZE = 300//GRID_SIZE
        self.RADIUS = int(self.SQUARESIZE/2.1)
        self.width = GRID_SIZE * self.SQUARESIZE
        self.height = (GRID_SIZE + 1) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        global Screen 
        Screen = self.screen

    
    def draw_Menu(self,players):
        pygame.draw.rect(self.screen, MENU_COLOR, (0, 0, self.width, self.height ))
        pygame.display.update()

        number_of_players = len(players)

        LRMargin = self.width / 20
        TDMargin = self.height / 30

        TOP = 20

        w = self.width / 2 
        h = (self.height - TOP*5) / number_of_players

        wm = w - 2 * LRMargin
        hm = h - 2 * TDMargin

        buttons1 = []
        buttons2 = []

        for i in range(number_of_players):
            x = LRMargin
            y = TOP+TDMargin+i*h
            
            B1 = Button(self.screen,x,y,w,h,wm,hm,players[i].name)
            B2 = Button(self.screen,x+w,y,w,h,wm,hm,players[i].name)

            buttons1.append(B1)
            buttons2.append(B2)
        
        names_left = 27
        names_up = 8

        PlayButton = Button(self.screen,x+w/2,TOP+TDMargin+(number_of_players)*h,w/2,h/5*4,wm,hm,"PLAY")

        Text.headline("Player 1",names_left,names_up,20)
        Text.headline("Player 2",names_left+w,names_up,20)

        pygame.display.update()

        return buttons1,buttons2,PlayButton
        
class Text:
    @staticmethod
    def headline(headline,x,y,size):
        def getFont(size):
            return pygame.font.SysFont("monospace", size)
        label = getFont(size).render(headline, 1 , BLACK)
        Screen.blit(label, (x, y))
        pygame.display.update()

class Button:
    def __init__(self,screen,x,y,w,h,wm,hm,name):
        self.screen = screen
        self.color = [YELLOW,RED]
        self.toggle = 0
        self.name = name
        self.x,self.y,self.w,self.h,self.wm,self.hm = x,y,w,h,wm,hm 
        self.Toggle()

    def Toggle(self):
        self.draw_button(self.color[self.toggle])
        self.toggle=1-self.toggle

    def UnToggle(self):
        self.draw_button(YELLOW)
        self.toggle=1

    def draw_button(self,color):
        x,y,w,h,wm,hm = self.x,self.y,self.w,self.h,self.wm,self.hm
        pygame.draw.rect(self.screen, BLACK, (x,y,wm,hm), 5)
        k = 1
        pygame.draw.rect(self.screen, color, (x+k,y+k,wm-k,hm-k))
        
        aName = self.name
        Text.headline(aName,x+5,y+10,25)

    def isClicked(self,event):
        posx = event.pos[0]
        posy = event.pos[1]
        x,y,w,h = self.x,self.y,self.w,self.h
        if(x<=posx and posx<=x+w):
            if(y<=posy and posy<=y+h):
                print(x,posx,x+w,y,posy,y+h)
                print(x)
                return 1
        return 0
    