import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method!")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self._is_valid_triangle():
            raise ValueError("The given sides do not form a valid triangle")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def _is_valid_triangle(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

# You can easily add more shapes by extending the Shape class
