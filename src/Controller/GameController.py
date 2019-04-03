import pygame
import sys

class GameController:
    def __init__(self, view):
        self.View = view
        self.run()

    
    def run(self):
        
        while(True):
            TicTacToeButton, Connect4Button = self.View.draw_game()


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
