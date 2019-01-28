from os import system
import numpy as np
import pygame
import random
import sys
from TicTacToe import TicTacToe

from RandomBot import RandomBot
from HumanPlayer import HumanPlayer

if __name__ == '__main__':
    A_TicTacToe = TicTacToe(5,10,RandomBot,RandomBot)
    A_TicTacToe.run()
    
