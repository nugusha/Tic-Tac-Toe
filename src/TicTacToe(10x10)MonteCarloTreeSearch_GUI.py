import sys
sys.path.append('./Controller')
from TicTacToe import TicTacToe
from HumanPlayer import HumanPlayer
from MonteCarloTreeSearchPlayer import MonteCarloTreeSearchPlayer

if __name__ == '__main__':
    p1 = MonteCarloTreeSearchPlayer("MCTS1")
    p2 = MonteCarloTreeSearchPlayer("MCTS2")
    hp = HumanPlayer("Nugusha")
    A_TicTacToe = TicTacToe(3,3,p1,p2)
    A_TicTacToe.run()