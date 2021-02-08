class Character:
    def __init__ (self, health, power):
        self.health = health
        self.power = power
    
    def alive(self):
        self.health > 0
        print(self.health)

class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        Character.__init__(self, health, power)
    
    # hero attacking goblin
    def attack(self, goblin):
        goblin.health -= self.power
        print("You do %d damage to the goblin." % (self.power))


    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))


class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        Character.__init__(self, health, power)
    
    # goblin attacking hero
    def attack(self, hero):
        hero.health -= self.power
        print(f'The goblin does {self.power} damage to you.')
    
    def print_status(self):
        print(f"The goblin has {self.health} health and {self.power} power.")



hero = Hero(10, 5)
goblin = Goblin(6, 2)
# need it in integer form, don't need the quotation

hero.print_status()
goblin.print_status()

hero.alive()
# when it says bound blahhh, you are probably printing the whole thing again