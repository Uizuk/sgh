class Square:
    def __init__(self, a):
        self.a=a
    def set_side(self, a):
        self.a=a
    def field(self):
        return self.a*self.a
    
k = Square(5)
k.field()