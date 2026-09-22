class Shape:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Shape:", self.name)


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = Rectangle("Rectangle", 10, 5)

r.display()
print("Area:", r.area())