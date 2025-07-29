import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
circle = Circle(7)

print(f"Radius          : {circle.radius}")
print(f"Area            : {circle.area():.2f}")
print(f"Circumference   : {circle.circumference():.2f}")