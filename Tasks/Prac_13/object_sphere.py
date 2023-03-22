import math


class Sphere:
    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return volume

    def get_square(self):
        square = 4 * math.pi * (self.radius ** 2)
        return square

    def get_radius(self):
        return self.radius

    def get_center(self):
        center = (self.x, self.y, self.z)
        return center

    def set_radius(self, r):
        self.radius = r
        return None

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return None

    def is_point_inside(self, x, y, z):
        if (self.x - self.radius < x < self.x + self.radius) and (self.y - self.radius < y < self.y + self.radius) and (self.z - self.radius < z < self.z + self.radius):
            return True
        else:
            return False


s0 = Sphere(0.5)
print(s0.get_center())
print(s0.get_volume())
print(s0.is_point_inside(0, -1.5, 0))
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0))
print(s0.get_radius())
