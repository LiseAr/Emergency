
class Employee:

    def __init__(self,id):
        self.id = id
        self.occupied = False
    
    def reserve(self):
        self.occupied = True

    def release(self):
        self.occupied = False

    