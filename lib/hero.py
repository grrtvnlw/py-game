from lib.Character import Character
import random

class Hero(Character):
    def __init__(self, name):
        super().__init__(name, 100, 5)

    def attack(self, target):
        double_damage = random.random() <= 0.2
        while double_damage:
            print(f"{self.name}'s power is doubled!")
            self.power *= 2
            super().attack(target)
            double_damage = False
        self.power = 5
        super().attack(target)