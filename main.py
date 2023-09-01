# Generate a base class animal
import numpy
from numpy import random


class Animal:

    def __init__(self, name, weight):
        self.name = name

        self.weight = weight

        self.hunger = 0

        self.health = 100

    def feed(self):
        self.hunger -= 1

    def check_health(self):
        self.health -= 1

    def __str__(self):
        return f"{self.name} has a weight of {self.weight} kg, and has a health of {self.health} and a hunger of {self.hunger}"


# Generate a class for a dog

class Dog(Animal):

    def __init__(self, name, weight):
        super().__init__(name, weight)

        self.hunger = 10

        self.health = 80

    def bark(self):
        print("Woof")

    def wag_tail(self):
        print("Wag wag")

    def __str__(self):
        return f"{self.name} has a weight of {self.weight} kg, and has a health of {self.health} and a hunger of {self.hunger}"


# Generate a class for a cat

class Cat(Animal):

    def __init__(self, name, weight):
        super().__init__(name, weight)

        self.hunger = 5

        self.health = 90

    def meow(self):
        print("Meow")

    def purr(self):
        print("Purr")

    def __str__(self):
        return f"{self.name} has a weight of {self.weight} kg, and has a health of {self.health} and a hunger of {self.hunger}"


if __name__ == '__main__':
    objects = []
    for i in range(10):
        rand_num = random.random()
        if rand_num > 0.5:
            objects.append(Dog(f"Dog{i}", random.randint(20, 70)))
        else:
            objects.append(Cat(f"Cat{i}", random.randint(10, 20)))

    print("\n".join([f"{str(obj)}" for obj in objects]))
