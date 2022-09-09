"""
Create a 2D vector and use it t create another class representing a 3D vector.
"""


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printVector(self):
        return ("{}x + {}y ".format(self.x,self.y))


class Vector3D(Vector2D):
    def __init__(self, x, y, z):

        super().__init__(x, y)
        self.z = z

    def printVector(self):
        return ("{}x + {}y + {}z ".format(self.x,self.y,self.z))

        

v2 = Vector2D(2,3)
v3 = Vector3D(11,2,3)
print(v2.printVector())
print(v3.printVector())