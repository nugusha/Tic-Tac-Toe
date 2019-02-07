import sys
import pygame
sys.path.append('./Controller')
sys.path.append('./View')
from MainController import MainController
from RandomBot import RandomBot
from HumanPlayer import HumanPlayer
from MiniMaxPlayer import MiniMaxPlayer
from MonteCarloTreeSearchPlayer import MonteCarloTreeSearchPlayer

if __name__ == '__main__':

    PLAYERS = []
    PLAYERS.append(HumanPlayer())
    PLAYERS.append(MonteCarloTreeSearchPlayer())
    PLAYERS.append(MiniMaxPlayer())
    PLAYERS.append(RandomBot())


    MENU = MainController(3, PLAYERS)
    RESULT = MENU.run()
    print(RESULT)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()
