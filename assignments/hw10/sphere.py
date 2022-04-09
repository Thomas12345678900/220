from math import*
class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        self.sphere_area = 4 * (pi * (self.radius ** 2))
        return self.sphere_area

    def volume(self):
        self.sphere_volume = (4/3) * (pi * (self.radius ** 3))
        return self.sphere_volume
