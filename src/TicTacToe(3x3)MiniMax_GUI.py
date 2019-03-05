import sys
sys.path.append('./Controller')
from TicTacToe import TicTacToe
from MiniMaxPlayer import MiniMaxPlayer
from MiniMaxPlayerV2 import MiniMaxPlayerV2

if __name__ == '__main__':
    p1 = MiniMaxPlayer()
    p2 = MiniMaxPlayerV2()
    A_TicTacToe = TicTacToe(3,3,p1,p2)
    A_TicTacToe.run()