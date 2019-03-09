import numpy as np
import math
from RandomBot import RandomBot
from TicTacToe import TicTacToeStatic
from PrioritizeMoves import PrioritizeMoves

class Node:
    def __init__(self,s,cnt,x=1, parent=None):
        self.s = np.array(s)
        self.parent = parent 
        self.c= [] 
        self.x=x 
        self.N=0 
        self.w=0 
        self.cnt = cnt

    def expand(self):
        status = TicTacToeStatic.Status(self.s)
        if(status != None):
            return

        moves = TicTacToeStatic.available_moves(self.s)
        NTWG = TicTacToeStatic.getNTW()
        PM = PrioritizeMoves(NTWG,len(self.s))
        PM_moves = PM.PrioritizeMoves(self.s,self.x,moves)

        if(moves!=PM_moves):
            #print(moves,PM_moves)
            moves = PM_moves
        if(self.cnt<=1000):
            moves = TicTacToeStatic.removecopies(self.s,moves)

        # print('--------------------')
        # ss= self.s.copy()
        # for move in moves:
        #     ss[move[0]][move[1]]=9
        # print(ss)
        #print(self.x, " [[[[[")
        #input()
        turn = self.x
        for move in moves:
            new_s = self.s.copy()
            r = move[0]
            c = move[1]
            new_s[r,c] = turn
            next = Node(new_s,self.cnt+1,turn*-1,self)
            self.c.append(next)

    def rollout(self):
        rand_play = RandomBot()
        cur_s = self.s
        turn = self.x
        lst = None
        cnt_now = self.cnt
        while(TicTacToeStatic.Status(cur_s, lst, cnt_now) is None):
            move = rand_play.make_a_move(cur_s)
            r = move // len(self.s)
            c = move % len(self.s)
            lst = r,c
            cnt_now += 1
            new_s = cur_s.copy()
            new_s[r,c]=turn
            cur_s = new_s
            turn*=-1

        e = TicTacToeStatic.Status(cur_s, lst, cnt_now)

        return e

    def backprop(self,e):
        self.w += e
        self.N += 1
        if(self.parent != None):
            self.parent.backprop(e)

    def selection(self):
        if(len(self.c) == 0):
            return self

        maxRate = -1
        ind = 0

        for i in range(len(self.c)):
            child = self.c[i]

            rate = 0
            if(child.N == 0):
                rate = float("inf")
            else:
                rate = UCB.UCB(self.x*child.w,child.N,self.N)
            if(rate > maxRate or i == 0):
                maxRate = rate
                ind = i
                
        n = self.c[ind]

        n = n.selection()
        return n

    def build_tree(self, n_iter=100):
        for i in range(n_iter):
            n = self.selection()
            n.expand()
            new_n = n.selection()
            e = new_n.rollout()
            new_n.backprop(e)

class UCB:
    @staticmethod
    def UCB(wi,ni,N,c=1.142):
        if(ni==0):
            b = float("inf")
        else:
            b = wi/ni + c*math.sqrt(math.log(N)/ni)
        return b

class MonteCarloTreeSearchPlayer:
    def __init__(self,name='MCTS'):
        self.name = name
        self.x = None

    def make_a_move(self,s,n_iter=100):
        s = np.array(s)
        length = len(s)
        cnt = 0
        for i in range(length):
            for j in range(length):
                if(s[i][j]!=0):
                    cnt += 1
                    

        if(cnt == 0):
            return (len(s)//2-1)*len(s)+(len(s)//2-1)
        
        moves = TicTacToeStatic.available_moves(s)
        NTWG = TicTacToeStatic.getNTW()
        PM = PrioritizeMoves(NTWG,len(s))
        PM_moves = PM.PrioritizeMoves(s,self.x,moves)

        if(moves!=PM_moves):
            #print(moves,PM_moves)
            moves = PM_moves
            #print(PM_moves," <---------------PM_moves")
            if(len(moves)==1):
                print("!!!")
                a = moves[0] 
                return a[0]*len(s)+a[1]
        
        

        root = Node(s,cnt,self.x)
        root.build_tree(n_iter)

        most = -1
        for child in root.c:
            if(child.N>most):
                most = child.N
                C = child
        
        r,c = 0,0
        length = len(s)
        for i in range(length):
            for j in range(length):
                if(root.s[i,j]!=C.s[i,j]):
                    r,c = i,j
        return r*len(s)+c