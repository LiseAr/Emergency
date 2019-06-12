from heapq import heappush

from src.Emergency import Emergency
from src.calc import get_dist_num
from src.Event import EndOfMedicalCare, EndOfScreening

class EndOfRegistration(Event):

    def __init__(self,  duration, time, patient, secretary):

        super().__init__(duration, time, patient)
    
        self.secretary = secretary

    def run(self, e: Emergency):
        
        if len(e.registration_queue) > 0:
            patient = e.registration_queue.pop()
            duration = get_dist_num(e.config['T']['CAD'])
            e.local_time += duration
            e.add_event_heap(EndOfRegistration(duration, e.local_time, 
                             patient, self.secretary))
        else:
            e.secretaries.add(self.secretary)
            self.secretary = None

        if (self.patient.priority == 5):
            if len(e.doctors) > 0:
                doctor = e.doctors.pop()
                duration = get_dist_num(e.config['T']['ATE'])
                e.local_time += duration
                e.add_event_heap(EndOfMedicalCare(duration, e.local_time, 
                                 self.patient, doctor))
            else: 
                entry = [self.patient.priority, e.count_mcq, self.patient]
                heappush(e.medical_care_queue, entry)
        else:
            if len(e.nurses) > 0:
                nurse = e.nurses.pop()
                duration = get_dist_num(e.config['T']['TRI'])
                e.local_time += duration
                e.add_event_heap(EndOfScreening(duration, e.local_time, self.patient,
                                                nurse))
            else:
                e.secreening_queue.append(self.patient)