import numpy as np
from TicTacToe import TicTacToeStatic
from random import shuffle

class Node:
    def __init__(self,s,cnt,x=1,c=None,m=None,v=None):
        self.s = s
        self.children = [] 
        self.x = x 
        self.move = m 
        self.score = v
        self.cnt = cnt

    def expand(self):
        status = TicTacToeStatic.Status(self.s)
        if(status != None):
            return
        moves = TicTacToeStatic.available_moves(self.s)
        #if(self.cnt<=3):
        #    moves = TicTacToeStatic.removecopies(self.s,moves)

        turn = self.x
        for move in moves:
            new_s = self.s.copy()
            r = move[0]
            c = move[1]
            new_s[r][c] = turn
            next = Node(new_s,self.cnt+1,turn*-1,None,(r,c))
            self.children.append(next)
        shuffle(self.children)
    def build_tree(self):
        self.expand()
        flag = 0
        for node in self.children:
            if(flag == 0):
                node.build_tree()
            else:
                node.score = 99
            if(node.score == self.x):
                self.score = node.score
                flag = 1 
        self.children = [x for x in self.children if x.score != 99 ]
        self.compute_score()
    def compute_score(self):
        status = TicTacToeStatic.Status(self.s)
        if(status != None):
            self.score = status
            return
            
        score1 = -1
        score2 = 1
        for child in self.children:
            if(self.x == 1):
                if(child.score > score1):
                    score1 = child.score
                if(child.score == 1):
                    break
            if(self.x == -1):
                if(child.score < score2):
                    score2 = child.score
                if(child.score == -1 ):
                    break
                    
        if(self.x == 1):
            self.score = score1
        elif(self.x == -1):
            self.score = score2

class MiniMaxPlayerV2:
    def __init__(self,name='MiniMaxV2'):
        self.name = name
        self.x = None
        self.now = None

    def make_a_move(self,ss):
        s=np.array(ss.copy())

        if(self.now==None):
            cnt = 0
            length = len(ss)
            for i in range(length):
                for j in range(length):
                    if(s[i][j]!=0):
                        cnt += 1

            self.now = Node(s,cnt,self.x)
            self.now.build_tree()
        else:
            a=0
            b=0
            A=0
            B=0
            for i in range(len(ss)):
                for j in range(len(ss)):
                    if(s[i][j] != self.now.s[i][j]):
                        if(self.now.s[i][j] == 0):
                            if(s[i][j] == self.x):
                                a,b = i,j
                            if(s[i][j] != self.x):
                                A,B = i,j
            
            self.now.s[a][b] = self.x

            for child in self.now.children:
                if(np.array_equal(child.s, self.now.s)):
                    self.now = child
                    #print("!!__!!")
                    break
                    
            self.now.s[A][B] = self.x*-1

            for child in self.now.children:
                if(np.array_equal(child.s, self.now.s)):
                    self.now = child
                    #print("!!_=_!!")
                    break

        r=0
        c=0
        for child in self.now.children:
            if(child.score==self.now.score):
                move = child.move
                r = move[0]
                c = move[1]
                break

        return r*len(s)+c