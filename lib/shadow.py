from lib.Character import Character
import random

class Shadow(Character):
    def __init__(self, name):
        super().__init__(name, 1, 2)

    def receive_damage(self, how_many_points):
        damage = random.random() <= 0.9
        if damage:
            how_many_points = 0
            super().receive_damage(how_many_points)
        else:
            super().receive_damage(how_many_points)
            
            
            