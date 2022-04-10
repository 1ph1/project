from turtle import left

from pygame import RESIZABLE
import game
import tkinter as tk

def close(event):
    return root.destroy()

def new_game(event):
    Game = tk.Toplevel()
    Game.geometry('{}x{}'.format(Game.winfo_screenwidth(),Game.winfo_screenheight()))
    lb = tk.Label(Game, text = 123)
    lb.pack()

root = tk.Tk()
root.resizable(False, False)
main = tk.Frame(root, width = 25)
main.pack(fill="both",expand=True)
#lb = Tk.Label(fr, text = game.SaveRoomsCreator().create_room().option())
NG = tk.Button(text = "Новая игра", width = 25)
NG.bind("<Button-1>", new_game)
OPTIONS = tk.Button(text = "Настройки", width = 25)
CLOSE = tk.Button(text = "Выход", width = 25)
CLOSE.bind("<Button-1>", close)
NG.pack()
OPTIONS.pack()
CLOSE.pack()

if __name__ == "__main__":
    root.mainloop()