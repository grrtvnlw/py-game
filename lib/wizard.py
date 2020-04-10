from lib.Character import Character
import random

class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, 90, 1)

    def death(self, target):
        print(f"{self.name} is 💀")
        target.coins += 6
        print(f"{target.name} gains 6 coins.")

    def attack(self, target):
        swap_power = random.random() > 0.5
        if swap_power:
            print(f"{self.name} swaps power with {target.name} during attack")
            self.power, target.power = target.power, self.power
        super().attack(target)
        if swap_power:
            self.power, target.power = target.power, self.power