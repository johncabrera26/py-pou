import random

class Pou:
    # iniciar
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = random.randint(0, 50)
        self.energy = random.randint(50, 100)
        self.happiness = random.randint(50, 100)
        self.health = 100
        self.alive = True

    def status(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Hunger:", self.hunger)
        print("Energy:", self.energy)
        print("Happiness:", self.happiness)
        print("Health:", self.health)

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nHunger: {self.hunger}\nEnergy: {self.energy}\nHappiness: {self.happiness}\nHealth: {self.health}"

    def play(self):
        self.hunger = self.minmax(self.hunger + random.randint(5, 10))
        self.energy = self.minmax(self.energy - random.randint(10, 20))
        self.happiness = self.minmax(self.happiness + random.randint(5, 10))
        self.health = self.minmax(self.health + random.randint(0, 5))

    def eat(self):
        self.hunger = self.minmax(self.hunger - random.randint(10, 20))
        self.energy = self.minmax(self.energy + random.randint(5, 10))
        self.happiness = self.minmax(self.happiness + random.randint(0, 3))
        self.health = self.minmax(self.health + random.randint(0, 5))

    def sleep(self):
        self.hunger = self.minmax(self.hunger + random.randint(5, 10))
        self.energy = self.minmax(self.energy + random.randint(30, 60))
        self.happiness = self.minmax(self.happiness + random.randint(0, 3))
        self.health = self.minmax(self.health + random.randint(0, 5))

    
    def minmax(self, value):
        return max(0, min(100, value))

# add more methods

toto = Pou("Toto")

while True:
    option = input("What do you want to do? (play, eat, sleep, age_up, exit): ")

    if option == "play":
        toto.play()
    elif option == "eat":
        toto.eat()
    elif option == "sleep":
        toto.sleep()
    elif option == "age_up":
        toto.age_up()
    elif option == "exit":
        break

    print(toto)
