from heapq import heappop, heappush

class Queue():

    def __init__(self, priority=False):
        
        self.priority = priority
        self.queue = []
        
        # kpis
        # mean time
        self.total_time_in_queue = 0 
        self.total_patients_in_queue = 0 
        # mean size
        self.time_in_queue = 0
        self.acc_patients_x_time = 0

    @property
    def empty(self):
        return len(self.queue) == 0

    def insert(self, element, count=0):

        try:
            priority = element.time
        except Exception as _ :
            priority = element.priority

        if self.priority:
            self.add_priority_queue(priority, count, element)
        else:
            self.queue.append(element)

    def next(self):
        if self.priority:
            return heappop(self.queue)[-1]
        else:
            return self.queue.pop()

    def add_priority_queue(self, priority, count, entry):
        entry = [priority, count, entry]
        heappush(self.queue, entry)

    @property
    def size(self):
        return len(self.queue)

    def update_info_time(self, time):
        self.total_time_in_queue += time
        self.total_patients_in_queue += 1

    def update_info_size(self, current_time):
        time = current_time - self.time_in_queue
        self.acc_patients_x_time += time * self.size
        self.time_in_queue = current_time

    def mean_time(self):
        if self.total_patients_in_queue == 0:
            return 0
        return self.total_time_in_queue/self.total_patients_in_queue
        
    def mean_size(self, simulation_time):
        return self.acc_patients_x_time / simulation_time

    def aging(self):
        for i, e in enumerate(self.queue):
            if (e[2].age == 5) and (e[2].priority != 1):
                entry = self.queue.pop(i)
                entry[2].priority -= 1
                entry[2].age = 0
                heappush(self.queue, entry)
            else:
                e[2].age += 1