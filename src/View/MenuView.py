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
        self.players = players
        global Screen 
        Screen = self.screen
        self.buttons1 = []
        self.buttons2 = []

    
    def draw_Menu(self):
        pygame.draw.rect(self.screen, MENU_COLOR, (0, 0, self.width, self.height ))
        pygame.display.update()

        number_of_players = len(self.players)

        Q1 = self.width / 3
        Q3 = self.width / 3 * 2

        LRMargin = self.width / 20
        TDMargin = self.height / 30

        TOP = 20

        w = self.width / 2 
        h = (self.height - TOP*5) / number_of_players

        wm = w - 2 * LRMargin
        hm = h - 2 * TDMargin

        for i in range(number_of_players):
            x = LRMargin
            y = TOP+TDMargin+i*h
            
            B1 = Button(self.screen,x,y,w,h,wm,hm,self.players[i].name)
            B2 = Button(self.screen,x+w,y,w,h,wm,hm,self.players[i].name)
            B1.Toggle()
            B2.Toggle()

            self.buttons1.append(B1)
            self.buttons2.append(B2)
        
        names_left = 27
        names_up = 8

        PlayButton = Button(self.screen,x+w/2,TOP+TDMargin+(number_of_players)*h,w/2,h/5*4,wm,hm,"PLAY")
        PlayButton.Toggle()

        Text.headline("Player 1",names_left,names_up,20)
        Text.headline("Player 2",names_left+w,names_up,20)

        pygame.display.update()
        
        flag = 0
        b1p = None
        b2p = None

        while(flag==0):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit()
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if(b1p!=None and b2p!=None):
                        if(PlayButton.isClicked(event)==1):
                            flag = 1
                    for i,b in enumerate(self.buttons1):
                        if(b.isClicked(event)>0):
                            b1p = self.players[i]
                            for bb in self.buttons1:
                                bb.UnToggle()
                            b.Toggle()
                    for i,b in enumerate(self.buttons2):
                        if(b.isClicked(event)>0):
                            b2p = self.players[i]
                            for bb in self.buttons2:
                                bb.UnToggle()
                            b.Toggle()

        print("!!!")


        A_TicTacToe = TicTacToe(3,3,b1p,b2p)
        A_TicTacToe.run()

        pygame.time.wait(30000)

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
    