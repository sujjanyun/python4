class Character:
    def __init__ (self, health, power):
        self.health = health
        self.power = power
    
    def alive(self, health):
        self.health > 0
        print(self.health)

class Hero(Character):
    def __init__(self, health, power, armor):
        self.health = health
        self.power = power
        self.armor = 4
        Character.__init__(self, health, power)
    
    # hero attacking goblin
    def attack(self, goblin):
        goblin.health -= self.power
        print("You do {self.power} damage to the goblin.")

    def print_status(self):
        print("You have {self.health} health and {self.power} power.")

    # items
    def store(self, health, power):
        print("Yoo Hoo, Big Summer Blowout! Welcome to Wandering Oaken's Trading Post and Sauna. What would you like to buy today?")
        item = input("""supertonic
        armor,
        evade,
        escape rope,
        aslan's sword""")
        if item == ("supertonic"):
            self.health == 10
        elif item == ("armor"):
            


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

class Medic(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        Character.__init__(self, health, power)

class Shadow(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        Character.__init__(self, health, power)

class Zombie(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def alive(self):
        self.health > -5
        print(self.health)




hero = Hero(10, 5)
goblin = Goblin(6, 2)
medic = Medic()
shadow = Shadow()
zombie = Zombie
# need it in integer form, don't need the quotation

hero.print_status()
goblin.print_status()
hero.store()

hero.alive()
# when it says bound blahhh, you are probably printing the whole thing again