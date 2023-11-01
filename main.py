class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Bird(Animal):
    def make_sound(self):
        print("Tweet")

def animal_sounds(animals):
    for animal in animals:
        animal.make_sound()

dog, cat, bird = Dog(), Cat(), Bird()

animals = [dog, cat, bird]

animal_sounds(animals)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(1, 4)
result = v1 + v2  # Результат: Vector(3, 7)
