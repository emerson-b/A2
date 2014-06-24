import random
from animal_class import *


class Sheep(Animal):
    """a sheep"""

    def __init__(self,name):
        super().__init__(10,6,7,name) #growth 1, ln 3, wn 6
        self._type = "Sheep"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need:
                self._weight += self._growth_rate * 2
            elif self._status == "Child" and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            else:
                self._weight = self._growth_rate
            self._days_growing += 1
            self._update_status()
            
def main():
    name = enter_name()
    sheep_animal = Sheep(name)
    print(sheep_animal.report())
    manual_grow(sheep_animal)
    print(sheep_animal.report())

if __name__ == "__main__":
    main()
    
