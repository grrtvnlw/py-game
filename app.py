"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. visit store
4. flee

"""
from lib.hero import Hero
from lib.goblin import Goblin
from lib.zombie import Zombie
from lib.medic import Medic
from lib.shadow import Shadow
from lib.wizard import Wizard
from lib.engine import main_menu, store_menu, shop
from lib.battle import do_battle

Hero = Hero("Lancelot")
Enemy = Zombie("Reggie")

def main():

    while Enemy.is_alive() and Hero.is_alive():
        Enemy.print_status()
        Hero.print_status()
        user_input = main_menu()
        #if user_input == "1":
        if user_input == "1":
            do_battle(Hero, Enemy)
        elif user_input == "2":
            # Hero does nothing, enemy attacks
            Enemy.attack(Hero)
            Hero.is_alive()
        elif user_input == "3":
            while True:
                store_input = store_menu()
                if store_input == "1":
                    print(f"{Hero.name} has {Hero.coins} coins")
                elif store_input == "2":
                    shop(Hero)
                else:
                    print("Thanks for coming in. Stay safe out there.")
                    break
        elif user_input == "4":
            print("Thanks for playing! Farewell.")
            break
        else:
            print("Invalid input %r" % user_input)
            
        Hero.is_alive()
        Enemy.is_alive()
main()