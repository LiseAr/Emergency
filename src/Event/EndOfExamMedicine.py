
class EndOfExamMedicine(Event):

    def __init__(self,  duration, time, patient, nurse):
        
        super().__init__(duration, time, patient)
    
        self.nurse = nurse