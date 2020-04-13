from lib.hero import Hero
from lib.goblin import Goblin
from lib.zombie import Zombie
from lib.medic import Medic
from lib.shadow import Shadow
from lib.wizard import Wizard

def battle_menu(hero, enemy):
    b_menu = f"""

    Welcome to the Battlefield It's {hero.name} versus {enemy.name}!
    1. Check Stats
    2. Fight Enemy
    3. Check Inventory
    4. Do Nothing
    5. Flee
    > 

    """
    print(b_menu)
    return input()

def do_battle(hero, enemy):
    print("=====================")
    print(f"{hero.name} faces {enemy.name}")
    print("=====================")
    while True:
        battle_input = battle_menu(hero, enemy)
        if battle_input == "1":
            hero.print_status()
            enemy.print_status()
        if battle_input == "2":
            # Hero attacks enemy
            hero.attack(enemy)
            enemy.is_alive()

            if enemy.is_alive():
            # Enemy attacks hero
                enemy.attack(hero)
                hero.is_alive()
            else:
                enemy.death(hero)
            if not hero.is_alive():
                hero.death()
            hero.print_status()
            enemy.print_status()
        elif battle_input == "3":
            if hero.inventory == []:
                print(f"{hero.name} has 0 items in inventory.")
            else:    
                for each_item in hero.inventory:
                    print(f"{hero.name} has {each_item.name} in inventory.")
        elif battle_input == "4":
            enemy.attack(hero)
        elif battle_input == "5":
            print(f"{hero.name} lives to fight another day.")
            break
        else:
            print(f"Invalid input {battle_input}")
            continue 