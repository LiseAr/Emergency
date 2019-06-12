from src.Emergency import Emergency
from src.Event import EndOfRegistration
from src.calc import get_dist_num

class EndOfArrival(Event):

    def __init__(self,  duration, time, patient):
        
        super().__init__(duration, time, patient)
    
    def run(self, e: Emergency):
        
        if len(e.secretaries) != 0:
            secretary = e.secretaries.pop()
            duration = get_dist_num(e.config['T']['CAD'])
            e.local_time += duration
            e.add_event_heap(EndOfRegistration(duration, e.local_time, self.patient,
                                               secretary))
        else:
            e.registration_queue.append(self.patient)