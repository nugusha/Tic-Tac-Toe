import pygame

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

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
        Text.headline(aName,x+5,y+10,25,self.screen)

    def isClicked(self,event):
        posx = event.pos[0]
        posy = event.pos[1]
        x,y,wm,hm = self.x,self.y,self.wm,self.hm
        if(x<=posx and posx<=x+wm):
            if(y<=posy and posy<=y+hm):
                print(x,posx,x+wm,y,posy,y+hm)
                print(x)
                return 1
        return 0
    
       
class Text:
    @staticmethod
    def headline(headline,x,y,size,Screen):
        def getFont(size):
            return pygame.font.SysFont("monospace", size)
        label = getFont(size).render(headline, 1 , BLACK)
        Screen.blit(label, (x, y))
        pygame.display.update()
