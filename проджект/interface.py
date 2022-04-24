import server
import tkinter as tk
import random
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
        self.turns_count = 10
        self.foe_hp = 10
        self.spellvar = tk.IntVar()
        self.spell_list = []

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
        self.lb_foe = tk.Label(self.fr2, fg = "black", text = "враг")
        self.lb_foe_hp = tk.Label(self.fr2, fg = "black", text = self.foe_hp)

        self.lb_book1 = tk.Label(self.fr3, bg = "#e0e094", fg = "white", width = 100, height = 15)
        self.lb_turncount = tk.Label(self.fr3, bg = "brown", fg = "black", text = self.turns_count) 
        self.bt_turnend = tk.Button(self.fr3, bg = "brown", fg = "black", text = "Завершить ход") 
        #------Радиобатоны
        self.rb1 = tk.Radiobutton(self.fr3, bg = "#e0e094", fg = "black", variable = self.spellvar, value = 0, text = self.new_spell())
        self.rb2 = tk.Radiobutton(self.fr3, bg = "#e0e094", fg = "black", variable = self.spellvar, value = 1, text = self.new_spell())
        self.rb3 = tk.Radiobutton(self.fr3, bg = "#e0e094", fg = "black", variable = self.spellvar, value = 2, text = self.new_spell())
        #-----------------

        #------пустышки      
        self.f1 = tk.Label(self.fr3, text = "Пустышка", fg = "#E6E6E6")
        self.f2 = tk.Label(self.fr3, text = "Пустышка", fg = "#E6E6E6")
        self.f3 = tk.Label(self.fr3, text = "Пустышка", fg = "#E6E6E6")
        self.f4 = tk.Label(self.fr3, text = "Пустышка", fg = "#E6E6E6")
        self.f5 = tk.Label(self.fr3, text = "Пуст", fg = "#E6E6E6")
        self.f6 = tk.Label(self.fr3, text = "Пустышка", fg = "#E6E6E6")
        self.f7 = tk.Label(self.fr3, text = "Пустышка", fg = "#E6E6E6")
        self.f8 = tk.Label(self.fr3, text = "Пустышка", fg = "#E6E6E6")
        self.f9 = tk.Label(self.fr3, text = "Пустышка", fg = "#E6E6E6")
        self.f10 = tk.Label(self.fr3, text = "Пуст", fg = "#E6E6E6")
        #--------------

        self.fr1.pack(fill = tk.X)
        self.fr2.pack(fill = tk.BOTH)
        self.fr3.pack(side = "bottom", fill = tk.X)
        self.bt_menu.pack(side = "right")
        self.lb_hp.pack(side = "left")

        self.lb_foe_hp.pack(side = "bottom")
        self.lb_foe.pack(side="bottom")

        self.f5.grid(row=0,column=0)
        self.lb_turncount.grid(row = 0, column=1)
        self.f1.grid(row=0,column=2)
        self.f2.grid(row=0,column=3)
        self.f3.grid(row=0,column=4)
        self.f4.grid(row=0,column=5)
        self.lb_book1.grid(row=0,column=6,rowspan=3,columnspan=5)
        self.f6.grid(row=0,column=12)
        self.f7.grid(row=0,column=13)
        self.f8.grid(row=0,column=14)
        self.f10.grid(row=0,column= 15)
        self.bt_turnend.grid(row=0,column = 16)
        self.rb1.grid(row=0,column=6)
        self.rb2.grid(row=1,column=6)
        self.rb3.grid(row=2,column=6)
        
        self.bt_menu.bind("<Button-1>", self.second_menu)
        self.bt_turnend.bind("<Button-1>", self.end_turn)
    #lb = Tk.Label(fr, text = game.SaveRoomsCreator().create_room().option())

    def find_enemy(self):
        pass

    def new_spell(self):
        self.spells = list(server.data["spell"].keys())
        self.spell_choise = random.randint(0,len(self.spells)-1)
        self.right_spell = self.spells.pop(self.spell_choise)
        self.spell_list.append(self.right_spell)
        return self.right_spell

    def end_turn(self, event):
        if self.spellvar.get() == 0:
            self.foe_hp -= server.data["spell"][self.spell_list.pop(0)]
            
        elif self.spellvar.get() == 1:
            self.foe_hp -= server.data["spell"][self.spell_list.pop(1)]
        elif self.spellvar.get() == 2:
            self.foe_hp -= server.data["spell"][self.spell_list.pop(2)]
        self.lb_foe_hp.config(text = self.foe_hp)
        self.rb1.config(text = self.new_spell())
        self.rb2.config(text = self.new_spell())
        self.rb3.config(text = self.new_spell())

if __name__ == "__main__":
    game = GAME()
    game.root.mainloop()
