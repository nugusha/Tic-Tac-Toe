import sys
sys.path.append('./Controller')
from TicTacToe import TicTacToe
from RandomBot import RandomBot
from HumanPlayer import HumanPlayer

if __name__ == '__main__':
    p1 = HumanPlayer('Human')
    p2 = RandomBot('Bot')
    A_TicTacToe = TicTacToe(3,3,p1,p2)
    A_TicTacToe.run()
    
