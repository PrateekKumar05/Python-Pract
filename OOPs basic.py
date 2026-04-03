class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @property
    def area(self):
        return 3.14 * (self._radius ** 2)
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value
    
C = Circle(3)
print(C.area)
print(C.radius)
C.radius = 8
print(C.radius)
print(C.area)