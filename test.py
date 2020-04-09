from lib.hero import Hero
from lib.goblin import Goblin

Lancelot = Hero("Lancelot")
Doug = Goblin("Doug")

Doug.print_status()
Lancelot.print_status()

Lancelot.attack(Doug)