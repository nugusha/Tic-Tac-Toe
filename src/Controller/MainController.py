import pygame
import sys
from copy import deepcopy
from TicTacToe import TicTacToe
from RandomBot import RandomBot
from HumanPlayer import HumanPlayer
from MiniMaxPlayer import MiniMaxPlayer
from MonteCarloTreeSearchPlayer import MonteCarloTreeSearchPlayer
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
MENU_COLOR = (234, 255, 34)
needToWinDict = {3: 3, 10: 5}

class MainController:
    def __init__(self, view):
        self.View = view

    
    def run(self):
        players = []
        players.append(HumanPlayer())
        players.append(MonteCarloTreeSearchPlayer())
        players.append(MiniMaxPlayer())
        players.append(RandomBot())

        self.players = players
        while(True):
            self.View.__init__(3, self.players)
            buttons1,buttons2,PlayButton,GRID3,GRID10 = self.View.draw_Menu(self.players)
            
            flag = 0
            p1 = None
            p2 = None
            p3 = None

            while(flag==0):
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        sys.exit()
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        if(p1!=None and p2!=None and p3!=None):
                            if(PlayButton.isClicked(event)==1):
                                flag = 1
                                p3=2
                                
                        if (GRID3.isClicked(event)==1 and p3!=2):
                            GRID3.Toggle()
                            GRID10.UnToggle()
                            GRID_SIZE=3
                            p3=1

                        if (GRID10.isClicked(event)==1 and p3!=2):
                            GRID10.Toggle()
                            GRID3.UnToggle()
                            GRID_SIZE=10
                            p3=1
                    
                        for i,b in enumerate(buttons1):
                            if(b.isClicked(event)>0):
                                p1 = deepcopy(self.players[i])
                                for bb in buttons1:
                                    bb.UnToggle()
                                b.Toggle()
                        for i,b in enumerate(buttons2):
                            if(b.isClicked(event)>0):
                                p2 = deepcopy(self.players[i])
                                for bb in buttons2:
                                    bb.UnToggle()
                                b.Toggle()

            print("!!!")
            
            #             TicTacToe(needToWin, GRID_SIZE,player1,player2)
            A_TicTacToe = TicTacToe(needToWinDict[GRID_SIZE],GRID_SIZE,p1,p2,False)
            A_TicTacToe.run()

        pygame.time.wait(30000)
