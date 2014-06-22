import random
from animal_class import *


class Cow(Animal):
    """a cow"""

    def __init__(self):
        super().__init__(15,5,6) #growth 1, ln 3, wn 6
        self._type = "cow"

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
    cow_animal = Cow()
    print(cow_animal.report())
    manual_grow(cow_animal)
    print(cow_animal.report())

if __name__ == "__main__":
    main()
    
