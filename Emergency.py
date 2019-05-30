
class Emergency:

    def __init__(self, configuration_file):

        # global
        self.time = 0

        # sets of employee
        self.nurses = set()
        self.doctors = set()
        self.secretaries = set()

        # queues
        self.event_queue = list()
        self.registration_queue = list()
        self.secreening_queue = list()
        self.service_queue = list()
        self.exam_medicine_queue = list()

        # dict of distributions
        self.distributions = []

        self.build(configuration_file)
        self.start()

    def build(self, configuration_file):
        pass

    def start(self):
        
                
        
