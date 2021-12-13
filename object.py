class object:
    def __init__(self, mass, size, color, theda, gravity):
        self.mass = mass
        self.size = size
        self.color = color
        self.theda = theda
        self.gravity = gravity
                
    def math(self):
        self.theda = self.mass * self.gravity
        return self.theda