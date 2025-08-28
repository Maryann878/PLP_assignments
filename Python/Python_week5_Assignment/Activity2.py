# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Animal:
    def move(self):
        return "This animal moves somehow."

class Dog(Animal):
    def move(self):
        return "Running 🐕"

class Bird(Animal):
    def move(self):
        return "Flying 🐦"

class Fish(Animal):
    def move(self):
        return "Swimming 🐟"

# Usage
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())
