class Points(object):
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)
    
    def dot(self, no):
        return (self.x * no.x + self.y * no.y + self.z * no.z)

    def cross(self, no):
        x_component = (self.y * no.z) - (self.z * no.y)
        y_component = (self.z * no.x) - (self.x * no.z)
        z_component = (self.x * no.y) - (self.y * no.x)
        return Points(x_component, y_component, z_component)
    
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

