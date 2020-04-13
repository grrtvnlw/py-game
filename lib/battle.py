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
                while len(hero.inventory) != 0:  
                    for index in range(len(hero.inventory)):
                        print(f"{hero.name} has {index}: {hero.inventory[index].name} in inventory.")
                    inv_input = input("Use item? ").lower()
                    if inv_input == "y":
                        item_input = int(input("Choose an item by its index number: "))
                        if hero.inventory[item_input] in hero.inventory:
                            hero.inventory[item_input].apply(hero)
                            print(f"{hero.name} used {hero.inventory[item_input].name}!")
                            del hero.inventory[item_input]
                            hero.print_status()
                        else:
                            print("Double check your inventory!")
                    else:
                        break
                    
        elif battle_input == "4":
            enemy.attack(hero)
        elif battle_input == "5":
            print(f"{hero.name} lives to fight another day.")
            break
        else:
            print(f"Invalid input {battle_input}")
            continue 