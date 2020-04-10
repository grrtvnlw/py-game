from lib.Character import Character
import random

class Hero(Character):
    def __init__(self, name):
        super().__init__(name, 100, 5, 30)
        self.armor = 0
        self.evade = 0
        self.inventory = []

    def attack(self, target):
        double_damage = random.random() <= 0.2
        if double_damage:
            while double_damage:
                print(f"{self.name}'s power is doubled!")
                self.power *= 2
                super().attack(target)
                double_damage = False
            self.power = self.power
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
        if self.inventory == []:
            print(f"{self.name} has 0 items in inventory.")
        else:    
            for each_item in self.inventory:
                print(f"{self.name} has {each_item.name} in inventory.")
    
    def stash(self, item):
        self.inventory.append(item)
        print(f"{self.name} now has {item.name} in his pouch.")

    def buy(self, item):
        self.coins -= item.cost
        if item.name == "Tonic" or item.name == "SuperTonic":
            inp = input("Use now or use later? ")
            if inp == "now":
                item.apply(self)
            else:
                self.stash(item)
        else:
            item.apply(self)