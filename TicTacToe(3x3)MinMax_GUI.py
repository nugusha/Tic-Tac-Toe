from os import system
import numpy as np
import pygame
import random
import sys
sys.path.append('./Controller')
from TicTacToe import TicTacToe
from RandomBot import RandomBot
from HumanPlayer import HumanPlayer
from MiniMaxPlayer import MiniMaxPlayer

if __name__ == '__main__':
    p1 = MiniMaxPlayer(1)
    p2 = MiniMaxPlayer(2)
    A_TicTacToe = TicTacToe(3,3,p1,p2)
    A_TicTacToe.run()
