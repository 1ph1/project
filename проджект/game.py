from abc import ABC, abstractmethod

data = {
    "spell":{
        "fireball" : 15,
        "lightning shard" : 20,
        "earthkick" : 15,
        "aboba kick" : 50,
        "gigaDrill" : 30 
    }
}

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
        saveroom = "aboba"
        return saveroom
class Attackroom(Room):
    def option(self):
        return "AttackRoom"
class Strangeroom(Room):
    def option(self):
        return "StrangeRoom"

class Ecreator(ABC):
    def create_enemy(self):
        pass

    def operation(self):
        product = self.create_enemy(self)
        result = f"Creator: The same creator's code has just worked with {product}"
        return result

class ZombieEnemyCreator(Ecreator):
    def create_enemy(self):
        return Zombie()
class SkeletonEnemyCreator(Ecreator):
    def create_enemy(self):
        return Skeleton()
class GoblinEnemyCreator(Ecreator):
    def create_enemy(self):
        return Goblin()

class Enemy(ABC):
    def option(self):
        pass

class Zombie(Enemy):
    def option(self):
        zombie = [100,10]
        return zombie
class Skeleton(Enemy):
    def option(self):
        skeleton = [80, 20]
        return skeleton
class Goblin(Enemy):
    def option(self):
        goblin = [50,50]
        return goblin
