import sys
sys.path.append('./Controller')
sys.path.append('./View')
sys.path.append('./Model')
from TicTacToe import TicTacToe
from HumanPlayer import HumanPlayer
from MonteCarloTreeSearchPlayer import MonteCarloTreeSearchPlayer
from MonteCarloTreeSearchPlayerV2 import MonteCarloTreeSearchPlayerV2

if __name__ == '__main__':
    p1 = MonteCarloTreeSearchPlayer("MCTS1")
    p2 = MonteCarloTreeSearchPlayer("MCTS2")
    hp = HumanPlayer("Nugusha")
    A_TicTacToe = TicTacToe(10,10,p1,p2)
    A_TicTacToe.run()