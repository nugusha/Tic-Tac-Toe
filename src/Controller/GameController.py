import pygame
import sys
from GameView import GameView
from MainController import MainController

class GameController:
    def __init__(self):
        self.View = None
        self.run()

    
    def run(self):
        
        while(True):
            View = GameView(100)
            TicTacToeButton, Connect4Button = View.draw_game()


            ChosenGame = None
            GameCount = 2

            while(ChosenGame == None):
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        sys.exit()
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        if(TicTacToeButton.isClicked(event)):
                            ChosenGame = 1
                            TicTacToeButton.Toggle()
                        if(Connect4Button.isClicked(event)):
                            ChosenGame = 2
                            Connect4Button.Toggle()
                        print(ChosenGame)
            break

        pygame.time.wait(300)
