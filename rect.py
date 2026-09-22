class rect:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def displayArea(self):
        print(f"Area of rectangle is {self.area()}")


r1 = rect(10, 3)
r1.displayArea()