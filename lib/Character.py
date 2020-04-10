class Character():
    def __init__(self, name, health, power, coins=0):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def attack(self, target):
        print(f'{self.name} strikes {target.name}')
        target.receive_damage(self.power)

    def receive_damage(self, how_many_points):
        print(f'{self.name} receives {how_many_points} damage')
        self.health -= how_many_points

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True
    
    def death(self, target):
        print(f"{self.name} is 💀")
        target.coins += 5
        print(f"{target.name} gains 5 coins.")

    def print_status(self):
        print(f"{self.name} has {self.health} health.")
        print(f"{self.name} has {self.power} power.")
        