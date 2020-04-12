def main_menu():
    m_menu = """
    1. Fight Enemy
    2. Do Nothing
    3. Visit Store
    4. Flee
    >
    """
    print(m_menu)
    return input()
    
def store_menu():
    s_menu = """

    Welcome to the Store! What do you want to do?
    1. Check Coins
    2. Buy Items
    3. Get Back to the Battle
    > 

    """
    print(s_menu)
    return input()

class Tonic:
    cost = 5
    name = 'Tonic'
    def apply(self, target):
        target.health += 2
        print(f"{target.name}'s' health increased to {target.health}.")

class SuperTonic(Tonic):
    cost = 10
    name = "SuperTonic"
    def apply(self, target):
        target.health += 10
        print(f"{target.name}'s' health increased to {target.health}.")

class Sword:
    cost = 10
    name = 'Sword'
    def apply(self, target):
        target.power += 2
        print(f"{target.name}'s power increased to {target.power}.")

class Armor:
    cost = 10
    name = 'Armor'
    def apply(self, target):
        target.armor += 5
        print(f"{target.name}'s armor increased to {target.armor}.")

class Evade:
    cost = 10
    name = 'Evade'
    def apply(self, target):
        target.evade += 2
        print(f"{target.name}'s escapability increased to {target.evade}.")

items = [Tonic, SuperTonic, Sword, Armor, Evade]

def shop(target):
    while True:
        print("What would you like to purchase?")
        for i in range(len(items)):
            item = items[i]
            print(f"{i + 1}. {item.name}. Buy {item.name} for {item.cost} coins.")
        print("6. Back to store menu.\n")
        in_store_input = int(input("> "))
        if in_store_input == 6:
            break
        else:
            ItemToBuy = items[in_store_input - 1]
            item = ItemToBuy()
            if target.coins - item.cost >= 0:
                target.buy(item)
            else:
                print(f"You're broke! Go fight some enemies.")