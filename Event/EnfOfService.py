
class EndOfRegistration(Event):

    def __init__(self,  duration, time, patient, doctor):
        
        super().__init__(duration, time, patient)
    
        self.doctor = doctor

        
    