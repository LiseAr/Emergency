class Patient:

    def __init__(self, id, priority, exam_medicine):
        self.id = id
        self.original_priority = priority
        self.priority = priority
        self.exam_medicine = exam_medicine
        self.age = 0
        self.joined_queue = 0.0
        self.waiting_time = 0