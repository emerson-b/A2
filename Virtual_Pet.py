class VirtualPet:
    """ a representation of a pet """
    def __init__(self,name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        print("I have been born. My name is {0}".format(self.name))
        
    def talk(self):
        print("Hi, I'm your virtual pet")

    def feed(self,food):
        if food == "Cake":
            self.hunger = self.hunger + 2
            self.energy = self.energy + 2
        elif food == "Spaghetti":
            self.hunger = self.hunger + 4
            self.energy = self.energy + 3
        elif food == "Cookie Dough":
            self.hunger = self.hunger + 6
            self.energy = self.energy - 2
        
def main():
    name = input("Please enter a name for your pet: ")
    pet_one = VirtualPet(name)
    pet_one.talk()
    print(pet_one.energy)
    pet_one.feed("Cake")
    print(pet_one.energy)

if __name__ == "__main__":
    main()
