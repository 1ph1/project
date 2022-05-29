import server
import tkinter as tk
import random
from PIL import Image, ImageTk

class GAME:

    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.main = tk.Frame(self.root, width = 25)
        self.CNT = tk.Button(text = "Загрузить сохранение", width = 25)
        self.NG = tk.Button(text = "Играть", width = 25)
        self.OPTIONS = tk.Button(text = "Настройки", width = 25)
        self.CLOSE = tk.Button(text = "Выход", width = 25)

        self.main.pack(fill="both",expand=True)
        self.CNT.pack()
        self.NG.pack()
        self.OPTIONS.pack()
        self.CLOSE.pack()

        self.CNT.bind("<Button-1>", self.continue_play)
        self.NG.bind("<Button-1>", self.new_game)
        self.OPTIONS.bind("<Button-1>", self.option)
        self.CLOSE.bind("<Button-1>", self.close)

        self.game_level = "normal"
        self.hp = 100
        self.turns_count = 5
        self.foe_hp = 10
        self.spellvar = tk.IntVar()
        self.spell_list = []
        self.zombie = server.ZombieEnemyCreator().create_enemy().option()
        self.skeleton = server.SkeletonEnemyCreator().create_enemy().option()
        self.goblin = server.GoblinEnemyCreator().create_enemy().option()
        self.attack = ""
        self.save = 0
        self.e_count = 0

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

        self.btac.bind("<Button-1>", self.change)

    def change(self, event):
        if self.var.get() == 0:
            self.game_level = "easy"
        elif self.var.get() == 1:
            self.game_level = "normal"
        else:
            self.game_level = "hard"

    def second_menu(self, event):
        self.menu = tk.Toplevel()
        self.lb_diff = tk.Label(self.menu, text = f"Сложность: {self.game_level}")
        self.CLOSE = tk.Button(self.menu, text = "Выход", width = 25)
        self.SAVE = tk.Button(self.menu, text = "Сохранить", width = 25)
        self.lb_diff.pack()
        self.CLOSE.pack()
        self.SAVE.pack()
        self.CLOSE.bind("<Button-1>", self.close)
        self.SAVE.bind("<Button-1>", self.save_progress)

    def new_game(self, event):
        self.Game = tk.Toplevel()
        self.Game.attributes('-fullscreen', True)

        self.fr1 = tk.Frame(self.Game, height = 400)
        self.fr2 = tk.Frame(self.Game)
        self.fr3 = tk.Frame(self.Game, height = 300, bg = "#d8d8d8")

        self.bt_menu = tk.Button(self.fr1, text = "меню")
        self.lb_hp = tk.Label(self.fr1, text = f"{self.hp}/100")
        self.lb_e_count = tk.Label(self.fr1, text = f"Количество убитых врагов: {self.e_count}")

        self.lb_pl = tk.Label(self.fr2, text = "Игрок", fg = "blue")
        self.lb_foe = tk.Label(self.fr2, fg = "black", text = "враг", bg = "#d8d8d8")
        self.lb_foe_hp = tk.Label(self.fr2, fg = "black", text = self.foe_hp)

        self.img_bt_end = tk.PhotoImage(file='end_turn_bt.png')

        self.lb_book1 = tk.Label(self.fr3, bg = "#e0e094", fg = "white", width = 100, height = 15)
        self.lb_turncount = tk.Label(self.fr3, bg = "green", fg = "black", text = self.turns_count) 
        self.bt_turnend = tk.Button(self.fr3, image = self.img_bt_end) 

        #self.lb_grandline = tk.Label(self.fr2, bg="#7A7666", width = 15)
        #------Радио батоны
        self.rb1 = tk.Radiobutton(self.fr3, bg = "#e0e094", fg = "black", variable = self.spellvar, value = 0, text = self.new_spell())
        self.rb2 = tk.Radiobutton(self.fr3, bg = "#e0e094", fg = "black", variable = self.spellvar, value = 1, text = self.new_spell())
        self.rb3 = tk.Radiobutton(self.fr3, bg = "#e0e094", fg = "black", variable = self.spellvar, value = 2, text = self.new_spell())
        #-----------------
        self.img = tk.PhotoImage(file='skelet.png')
        self.lb_img = tk.Label(self.fr2, image=self.img)
        #------пустышки      
        self.f1 = tk.Label(self.fr3, text = "Пустышка", fg = "#d8d8d8", bg = "#d8d8d8")
        self.f2 = tk.Label(self.fr3, text = "Пустышка", fg = "#d8d8d8", bg = "#d8d8d8")
        self.f3 = tk.Label(self.fr3, text = "Пустышка", fg = "#d8d8d8", bg = "#d8d8d8")
        self.f4 = tk.Label(self.fr3, text = "Пустышка", fg = "#d8d8d8", bg = "#d8d8d8")
        self.f5 = tk.Label(self.fr3, text = "Пуст", fg = "#d8d8d8", bg = "#d8d8d8")
        self.f6 = tk.Label(self.fr3, text = "Пустышка", fg = "#d8d8d8", bg = "#d8d8d8")
        self.f7 = tk.Label(self.fr3, text = "Пустышка", fg = "#d8d8d8", bg = "#d8d8d8")
        self.f8 = tk.Label(self.fr3, text = "Пустышка", fg = "#d8d8d8", bg = "#d8d8d8")
        self.f9 = tk.Label(self.fr3, text = "Пустышка", fg = "#d8d8d8", bg = "#d8d8d8")
        self.f10 = tk.Label(self.fr3, text = "Пуст", fg = "#d8d8d8", bg = "#d8d8d8")
        #--------------

        self.fr1.pack(fill = tk.X)
        self.fr2.pack(fill = tk.BOTH)
        self.fr3.pack(side = "bottom", fill = tk.X)
        self.bt_menu.pack(side = "right")
        self.lb_hp.pack(side = "left")
        self.lb_e_count.pack(side = "left")

        #self.lb_grandline.pack(side="bottom", fill= tk.X)
        self.lb_img.pack(side="bottom")
        self.lb_foe_hp.pack(side = "bottom")
        self.lb_foe.pack(side="bottom")

        self.f5.grid(row=0,column=0)
        self.lb_turncount.grid(row = 0, column=1, rowspan = 4, columnspan=3)
        self.f1.grid(row=0,column=2)
        self.f2.grid(row=0,column=3)
        self.f3.grid(row=0,column=4)
        self.f4.grid(row=0,column=5)
        self.lb_book1.grid(row=0,column=6,rowspan=3,columnspan=5)
        self.f6.grid(row=0,column=12)
        self.f7.grid(row=0,column=13)
        self.f8.grid(row=0,column=14)
        self.f10.grid(row=0,column= 15)
        self.bt_turnend.grid(row=1,column = 16)
        self.rb1.grid(row=0,column=6)
        self.rb2.grid(row=1,column=6)
        self.rb3.grid(row=2,column=6)
        
        
        self.bt_menu.bind("<Button-1>", self.second_menu)
        self.bt_turnend.bind("<Button-1>", self.end_turn)
        if self.save == 1:
            self.lb_foe.config(text = self.attack)
            if self.attack == "zombie":
                self.img.config(file = "zombie.png")
            elif self.attack == "skeleton":
                self.img.config(file = "skelet.png")
            else:
                self.img.config(file = "goblin.png")
            self.lb_foe_hp.config(text = self.foe_hp)
            self.lb_hp.config(text = f"{self.hp}/100")
            self.lb_e_count.config(text = f"Количество убитых врагов: {self.e_count}")

    def new_spell(self):
        self.spells = list(server.data["spell"].keys())
        self.spell_choise = random.randint(0,len(self.spells)-1)
        self.right_spell = self.spells.pop(self.spell_choise)
        self.spell_list.append(self.right_spell)
        return self.right_spell

    def end_turn(self, event):
        self.turns_count -= 1
        if self.spellvar.get() == 0:
            damage = server.data["spell"][self.spell_list.pop(0)]
            self.foe_hp -= damage
        elif self.spellvar.get() == 1:
            self.foe_hp -= server.data["spell"][self.spell_list.pop(1)]
        elif self.spellvar.get() == 2:
            damage = server.data["spell"][self.spell_list.pop(2)]
            self.foe_hp -= damage

        if self.foe_hp <= 0:
            self.e_count += 1
            self.lb_e_count.config(text = f"Количество убитых врагов: {self.e_count}")
            self.zombie = server.ZombieEnemyCreator().create_enemy().option()
            self.skeleton = server.SkeletonEnemyCreator().create_enemy().option()
            self.goblin = server.GoblinEnemyCreator().create_enemy().option()
            enemy_choise = random.randint(0,2)
            if enemy_choise == 0:
                self.attack = "zombie"
                self.img.config(file = "zombie.png")
                self.foe_hp = self.zombie.pop(0)
                self.lb_foe.config(text = "Zombie")
            elif enemy_choise == 1:
                self.attack = "skeleton"
                self.img.config(file = "skelet.png")
                self.foe_hp = self.skeleton.pop(0)
                self.lb_foe.config(text = "Skeleton")
            else:
                self.attack = "goblin"
                self.img.config(file = "goblin.png")
                self.foe_hp = self.goblin.pop(0)
                self.lb_foe.config(text = "Goblin")

        
        self.lb_foe_hp.config(text = self.foe_hp)
        self.spell_list.clear()
        self.rb1.config(text = self.new_spell())
        self.rb2.config(text = self.new_spell())
        self.rb3.config(text = self.new_spell())
        if self.turns_count == 0:
            if self.attack == "zombie":
                if self.game_level == "easy":
                    self.hp -= self.zombie.pop(0)
                elif self.game_level == "normal":
                    damage = self.zombie.pop(0)
                    self.hp -= (damage * 2)
                else:
                    damage = self.zombie.pop(0)
                    self.hp -= (damage * 3)
                if self.hp <= 0:
                    self.gameover = tk.Toplevel()
                    self.lb_gameover = tk.Label(self.gameover, text = "Вы проиграли(")
                    self.CLOSE = tk.Button(self.gameover, text = "Закрыть игру", width = 25)
                    self.CLOSE.pack()
                    self.CLOSE.bind("<Button-1>", self.close)
                else:
                    self.turns_count = 5
                    self.lb_hp.config(text= f"{self.hp}/100")
            elif self.attack == "skeleton":
                if self.game_level == "easy":
                    self.hp -= self.skeleton.pop(0)
                elif self.game_level == "normal":
                    damage = self.skeleton.pop(0)
                    self.hp -= (damage * 2)
                else:
                    damage = self.skeleton.pop(0)
                    self.hp -= (damage * 3)
                if self.hp <= 0:
                    self.gameover = tk.Toplevel()
                    self.lb_gameover = tk.Label(self.gameover, text = "Вы проиграли(")
                    self.CLOSE = tk.Button(self.gameover, text = "Закрыть игру", width = 25)
                    self.CLOSE.pack()
                    self.CLOSE.bind("<Button-1>", self.close)
                else:
                    self.turns_count = 5
                    self.lb_hp.config(text=f"{self.hp}/100")
            elif self.attack == "goblin":
                if self.game_level == "easy":
                    self.hp -= self.skeleton.pop(0)
                elif self.game_level == "normal":
                    damage = self.skeleton.pop(0)
                    self.hp -= (damage * 2)
                else:
                    damage = self.skeleton.pop(0)
                    self.hp -= (damage * 3)
                if self.hp <= 0:
                    self.gameover = tk.Toplevel()
                    self.lb_gameover = tk.Label(self.gameover, text = "Вы проиграли(")
                    self.CLOSE = tk.Button(self.gameover, text = "Закрыть игру", width = 25)
                    self.CLOSE.pack()
                    self.CLOSE.bind("<Button-1>", self.close)
                else:
                    self.lb_hp.config(text=f"{self.hp}/100")
                    self.turns_count = 5
        self.lb_turncount.config(text = self.turns_count)

    def save_progress(self, event):
        opensave = open('saves.txt', 'w')
        enemy = self.attack
        fhp = self.foe_hp
        shp = self.hp
        diffcult = self.game_level
        e_count = self.e_count
        opensave.write(f"{enemy}\n")
        opensave.write(f"{str(fhp)}\n")
        opensave.write(f"{str(shp)}\n")
        opensave.write(f"{diffcult}\n")
        opensave.write(f"{e_count}\n")
        opensave.close()

    def continue_play(self, event):
        opensave = open('saves.txt')
        savesp = []
        for line in opensave:
            cur_save = line.replace("\n", "")
            savesp.append(cur_save)

        self.attack = savesp.pop(0)
        self.foe_hp = savesp.pop(0)
        print(self.foe_hp)
        self.hp = savesp.pop(0)
        self.game_level = savesp.pop(0)
        self.e_count = savesp.pop(0)
        self.save += 1

if __name__ == "__main__":
    game = GAME()
    game.root.mainloop()
