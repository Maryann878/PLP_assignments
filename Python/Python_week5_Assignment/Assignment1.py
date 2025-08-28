# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

# Base Class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery  # 🔒 encapsulated (private attribute)

    def get_battery(self):
        return f"{self.__battery}% battery remaining"

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        return f"Charging... now at {self.__battery}%"

    def info(self):
        return f"{self.brand} {self.model} - {self.get_battery()}"


# Inherited Class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, gpu_power):
        super().__init__(brand, model, battery)
        self.gpu_power = gpu_power

    def play_game(self, game):
        return f"Playing {game} 🎮 with GPU power {self.gpu_power}!"

    # Overriding (Polymorphism example too!)
    def info(self):
        return f"{self.brand} {self.model} (Gaming Edition) - {self.get_battery()}"
        

# Usage
phone1 = Smartphone("Samsung", "S24 Ultra", 80)
gaming_phone = GamingPhone("Asus", "ROG 7", 60, "Ultra-RTX")

print(phone1.info())
print(phone1.charge(15))
print(gaming_phone.info())
print(gaming_phone.play_game("Call of Duty"))
