
class EndOfRegistration(Event):

    def __init__(self,  duration, time, patient, secretary):

        super().__init__(duration, time, patient)
    
        self.secretary = secretary


    