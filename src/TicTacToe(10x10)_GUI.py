import sys
sys.path.append('./Controller')
from TicTacToe import TicTacToe
from RandomBot import RandomBot
from HumanPlayer import HumanPlayer

if __name__ == '__main__':
    p1 = RandomBot('Bot1')
    p2 = RandomBot('Bot2')
    A_TicTacToe = TicTacToe(5,10,p1,p2)
    A_TicTacToe.run()