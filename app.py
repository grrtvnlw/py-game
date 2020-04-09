"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
from lib.hero import Hero
from lib.goblin import Goblin
from lib.zombie import Zombie
from lib.medic import Medic
from lib.shadow import Shadow

Hero = Hero("Lancelot")
Enemy = Goblin("Goblin")

def main():

    while Enemy.is_alive() and Hero.is_alive():
        Enemy.print_status()
        Hero.print_status()
        print()
        print("What do you want to do?")
        print("1. fight %s" % Enemy.name)
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            Hero.attack(Enemy)
            Enemy.is_alive()
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if Enemy.is_alive():
            # Enemy attacks hero
            Enemy.attack(Hero)
            Hero.is_alive()
        else:
            Enemy.death()

        if not Hero.is_alive():
            Hero.death()
            
main()
