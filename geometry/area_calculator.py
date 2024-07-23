from geometry.shapes import Shape

def calculate_area(shape):
    if not isinstance(shape, Shape):
        raise TypeError("The shape must be an instance of the Shape class or its subclasses")
    return shape.area()
