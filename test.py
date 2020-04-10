"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. visit store
4. flee

"""
from lib.engine import Engine
from lib.hero import Hero
from lib.goblin import Goblin
from lib.zombie import Zombie
from lib.medic import Medic
from lib.shadow import Shadow

Hero = Hero("Lancelot")
Enemy = Goblin("Goblin")
engine = Engine()

store_menu = """

Welcome to the Store! What do you want to do?
1. Buy Items
2. Get Back to the Battle
> 
"""

def main():

    while Enemy.is_alive() and Hero.is_alive():
        Enemy.print_status()
        Hero.print_status()
        engine.start()
        
main()
