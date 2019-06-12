# import scipy.stats
from scipy import stats
from heapq import *

from .Entity import Secretary, Nurse, Patient, Doctor
from .Event import EndOfArrival 
from ..src.calc import get_dist_num, get_exam_medicine, get_priority
from ..src.data import read_config

class Emergency:

    def __init__(self, configuration_file):

        # global
        self.total_time = 0
        self.local_time = 0

        # sets of employee
        self.nurses = set()
        self.doctors = set()
        self.secretaries = set()

        # queues
        self.event_queue = []
        self.registration_queue = list()
        self.secreening_queue = list()
        self.exam_medicine_queue = list()
        self.medical_care_queue = []

        # config
        self.config = {}
        self.count_event = 0
        self.count_mcq = 0

        self.build(configuration_file)
        self.start()

    def start(self):

        if len(self.event_queue) > 0:
            self.next_event.run(self)

    def build(self, configuration_file):
        
        self.config = read_config(configuration_file)
        
        self.total_time = config['T']['TTS']
        self.create_employees()
        self.initialize_event_queue()

    def create_employees(self):
        config = self.config['Q']
        id = 1
        amount = int(config['MED'])
        for _ in range(amount):
            self.doctors.add(Doctor(id))
            id += 1
        amount = int(config['ENF'])
        for _ in range(amount):
            self.nurses.add(Nurse(id))
            id += 1
        amount = int(config['ATD'])
        for _ in range(amount):
            self.secretaries.add(Secretary(id))
            id += 1

    def initialize_event_queue(self):
        
        local_time = 0
        id = 1
        args = self.config['T']['CHE']

        while local_time < self.total_time:
            
            duration = get_dist_num(args)
            priority = get_priority()
            exam_medicine = get_exam_medicine()
            
            patient = Patient(id, priority, exam_medicine)
            id += 1
            local_time += duration
            self.add_event_heap(EndOfArrival(duration, local_time, patient))

    def add_event_heap(self, event):
        self.count += 1
        entry = [event.time, self.count_event, event]
        self.event_queue.headpush(entry)

    def next_event(self):
        return heappop(self.event_queue)