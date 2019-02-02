import sys
import pygame
sys.path.append('./Controller')
sys.path.append('./View')
from TicTacToe import TicTacToe
from RandomBot import RandomBot
from HumanPlayer import HumanPlayer
from MiniMaxPlayer import MiniMaxPlayer
from MonteCarloTreeSearchPlayer import MonteCarloTreeSearchPlayer
from MenuView import MenuView

if __name__ == '__main__':

    players = []
    players.append(HumanPlayer())
    players.append(MonteCarloTreeSearchPlayer())
    players.append(MiniMaxPlayer())
    players.append(RandomBot())


    Menu = MenuView(3,players)
    Menu.draw_Menu()


    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()
    
    