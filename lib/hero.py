from lib.Character import Character
import random

class Hero(Character):
    def __init__(self, name):
        super().__init__(name, 100, 5, 30)
        self.armor = 0
        self.evade = 0

    def attack(self, target):
        double_damage = random.random() <= 0.2
        if double_damage:
            while double_damage:
                print(f"{self.name}'s power is doubled!")
                self.power *= 2
                super().attack(target)
                double_damage = False
            self.power = 5
        else:
            super().attack(target)
    
    def receive_damage(self, how_many_points):
        avoid = self.evade / 10
        avoid_attack = random.random() < avoid
        if avoid_attack:
            print(f"{self.name} deftly dodges the attack and receives no damage.")
        else:
            total_damage = how_many_points - self.armor
            print(f'{self.name} receives {total_damage} damage')
            self.health -= total_damage

    def print_status(self):
        super().print_status()
        print(f"{self.name} has {self.coins} coins.")
        print(f"{self.name} has {self.armor} defense.")
        print(f"{self.name} has {self.evade} escapability.")

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)