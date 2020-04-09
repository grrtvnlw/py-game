from lib.Character import Character

class Zombie(Character):
    def __init__(self, name):
        super().__init__(name, 10, 5)

    def is_alive(self):
        if self.health <= 0:
            self.health = 10
        else:
            return True