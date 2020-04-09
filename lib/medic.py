from lib.Character import Character
import random

class Medic(Character):
    def __init__(self, name):
        super().__init__(name, 10, 2)

    def receive_damage(self, how_many_points):
        recup = random.random() <= 0.2
        if recup:
            super().receive_damage(how_many_points)
            print(f"{self.name} got a health boost of 2!")
            self.health += 2
        else:
            super().receive_damage(how_many_points)