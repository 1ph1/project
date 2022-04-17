import server
import tkinter as tk
class GAME:

    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.main = tk.Frame(self.root, width = 25)
        self.NG = tk.Button(text = "Новая игра", width = 25)
        self.OPTIONS = tk.Button(text = "Настройки", width = 25)
        self.CLOSE = tk.Button(text = "Выход", width = 25)


        self.main.pack(fill="both",expand=True)
        self.NG.pack()
        self.OPTIONS.pack()
        self.CLOSE.pack()

        self.NG.bind("<Button-1>", self.new_game)
        self.OPTIONS.bind("<Button-1>", self.option)
        self.CLOSE.bind("<Button-1>", self.close)

        self.game_level = "normal"
        self.hp = 100
        self.spells_count = 10

    def close(self, event):
        return self.root.destroy()

    def option(self, event):
        self.options = tk.Toplevel()
        self.var = tk.IntVar()
        self.var.set(1)
        self.lbl = tk.Label(self.options, text = "Выберите сложность")
        self.r1 = tk.Radiobutton(self.options, variable = self.var, value = 0, text = "Лёгкая сложность")
        self.r2 = tk.Radiobutton(self.options, variable = self.var, value = 1, text = "Нормальная сложность")
        self.r3 = tk.Radiobutton(self.options, variable = self.var, value = 2, text = "Сложная сложность")
        self.btac = tk.Button(self.options, text = "Применить настройки")

        self.lbl.pack()
        self.r1.pack()
        self.r2.pack()
        self.r3.pack()
        self.btac.pack()

        self.btac.bind("<button-1>", self.change)

    def change(self):
        if self.var.get() == 0:
            self.game_level = "easy"
        elif self.var.get() == 1:
            self.game_level = "normal"
        else:
            self.game_level = "hard"

    def second_menu(self, event):
        self.menu = tk.Toplevel()
        self.CLOSE = tk.Button(self.menu, text = "Выход", width = 25)
        self.CLOSE.pack()
        self.CLOSE.bind("<Button-1>", self.close)

    def new_game(self, event):
        self.Game = tk.Toplevel()
        self.Game.attributes('-fullscreen', True)
        self.fr1 = tk.Frame(self.Game, height = 400)
        self.fr2 = tk.Frame(self.Game)
        self.fr3 = tk.Frame(self.Game, height = 300)
        self.bt_menu = tk.Button(self.fr1, text = "меню")
        self.lb_hp = tk.Label(self.fr1, text = f"{self.hp}/100")
        self.lb_pl = tk.Label(self.fr2, text = "Игрок", fg = "blue")
        self.lb_foe = tk.Label(self.fr2, fg = "black")
        self.lb_book1 = tk.Label(self.fr3, bg = "gray", text = "123", width = 100, height = 15)
        self.fr1.pack(fill = tk.X)
        self.fr2.pack(fill = tk.BOTH)
        self.fr3.pack(side = "bottom", fill = tk.X)
        self.bt_menu.pack(side = "right")
        self.lb_hp.pack(side = "left")
        self.lb_pl.pack(side = "left")
        self.lb_foe.pack(side = "right")
        self.lb_book1.pack(side = "bottom")
        self.bt_menu.bind("<Button-1>", self.second_menu)
    #lb = Tk.Label(fr, text = game.SaveRoomsCreator().create_room().option())

    def find_enemy():
        pass

if __name__ == "__main__":
    game = GAME()
    game.root.mainloop()
