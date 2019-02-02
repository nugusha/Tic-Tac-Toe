import sys
sys.path.append('./Controller')
from TicTacToe import TicTacToe
from RandomBot import RandomBot
from HumanPlayer import HumanPlayer
from MiniMaxPlayer import MiniMaxPlayer

if __name__ == '__main__':
    p1 = MiniMaxPlayer()
    p2 = MiniMaxPlayer()
    A_TicTacToe = TicTacToe(3,3,p1,p2)
    A_TicTacToe.run()