from tkinter import *
from tkinter import ttk

class MainTkinter:

    def __init__(self, master):

        master.title('Play Game')
        master.config(relief = RIDGE)
        

        frame = ttk.Frame(master)
        frame.config(padding = (30, 15))
        frame.pack()
        playButton = ttk.Frame(master)
        playButton.config(padding = (30, 15))
        playButton.pack()

        player1 = ttk.Label(frame, text = "Player 1", padding = (30, 15)).grid(row = 0, column = 0)
        player2 = ttk.Label(frame, text = "Player 2", padding = (30, 15)).grid(row = 0, column = 1)

        players = ['Human', 'MCTS', 'MiniMax', 'Bot']

        for i in range(len(players)):
            ttk.Button(frame, text = players[i]).grid(row = i+1, column = 0)
            ttk.Button(frame, text = players[i]).grid(row = i+1, column = 1)

        ttk.Button(frame, text = '3x3').grid(row = len(players)+1, column = 0)
        ttk.Button(frame, text = '10x10').grid(row = len(players)+1, column = 1)
        ttk.Button(playButton, text = 'PLAY').grid()
            
def main():            
    
    root = Tk()
    app = MainTkinter(root)
    root.mainloop()
    
if __name__ == "__main__": main()
