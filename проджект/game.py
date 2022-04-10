from abc import ABC, abstractmethod

class Rcreator(ABC):
    def create_room(self):
        pass
    
    def operation(self):
        product = self.create_room(self)
        result = f"Creator: The same creator's code has just worked with {product}"
        return result

class SaveRoomsCreator(Rcreator):
    def create_room(self):
        return Saveroom()

class AttackRoomsCreator(Rcreator):
    def create_room(self):
        return Attackroom()

class StrangeRoomsCreator(Rcreator):
    def create_room(self):
        return Strangeroom()

class Room(ABC):
    def option(self):
        pass

class Saveroom(Room):
    def option(self):
        return "SaveRoom"
class Attackroom(Room):
    def option(self):
        return "AttackRoom"
class Strangeroom(Room):
    def option(self):
        return "StrangeRoom"

class Ecreator(ABC):
    def create_enemy(self):
        pass

class ZombieEnemyCreator(Ecreator):
    def create_enemy(self):
        return
class SkeletonEnemyCreator(Ecreator):
    def create_enemy(self):
        return
class GoblinEnemyCreator(Ecreator):
    def create_enemy(self):
        return

class Enemy(ABC):
    def option(self):
        pass

class Zombie(Enemy):
    def option(self):
        return "zombie"
class Skeleton(Enemy):
    def option(self):
        return "skeleton"
class Goblin(Enemy):
    def option(self):
        return "goblin"