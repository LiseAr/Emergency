
class Doctor(Employee):

    def __init__(self, id):
        
        super().__init__(id)

        self.idleness_time = 0.0
        