import sys
sys.path.append('./Controller')
from TicTacToe import TicTacToe
from RandomBot import RandomBot
from HumanPlayer import HumanPlayer
from MiniMaxPlayer import MiniMaxPlayer
from MonteCarloTreeSearchPlayer import MonteCarloTreeSearchPlayer

if __name__ == '__main__':
    result = 0
    dict = {}
    for i in range(10):
        p1 = MiniMaxPlayer()
        p2 = MonteCarloTreeSearchPlayer()
        A_TicTacToe = TicTacToe(3,3,p1,p2,True)
        result = A_TicTacToe.run()
        print(i,result)
        if(dict.get(result)==None):
            dict[result] = 1
        else:
            dict[result] += 1
    print (dict)