# Задание №1
class Device:
    def init(self, brand, model):
        self.brand = brand
        self.model = model

class CoffeeMachine(Device):
    def brew_coffee(self):
        print("Brewing coffee...")

class Blender(Device):
    def blend(self):
        print("Blending...")

class MeatGrinder(Device):
    def grind_meat(self):
        print("Grinding meat...")

# Задание №2
class Ship:
    def init(self, name, displacement):
        self.name = name
        self.displacement = displacement

class Frigate(Ship):
    def deploy_sonar(self):
        print("Deploying sonar...")

class Destroyer(Ship):
    def launch_missiles(self):
        print("Launching missiles...")

class Cruiser(Ship):
    def fire_cannons(self):
        print("Firing cannons...")
# Задание №1
class Square:
    def init(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

class Circle:
    def init(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

class CircleInSquare(Square, Circle):
    pass

# Задание №2
class Wheels:
    def roll(self):
        print("Wheels rolling...")

class Engine:
    def start(self):
        print("Engine starting...")

class Doors:
    def open(self):
        print("Doors opening...")

class Car(Wheels, Engine, Doors):
    pass

# Задание №3
class Shape:
    def show(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

class Square(Shape):
    def init(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        print(f"Square at ({self.x}, {self.y}) with side length {self.side_length}")


shapes = [Square(0, 0, 5)]


for shape in shapes:
    shape.save()

loaded_shapes = [Square(0, 0, 0)] * len(shapes) 
for i, shape in enumerate(loaded_shapes):
    loaded_shapes[i].load()

for shape in loaded_shapes:
    shape.show()