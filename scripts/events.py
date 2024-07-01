class Event:
    def __init__(self, run_id, parent_id, level, event_type, message, start_date=None, end_date=None):
        self.run_id = run_id
        self.parent_id = parent_id
        self.level = level
        self.event_type = event_type
        self.message = message
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self):
        return {
            'run_id': self.run_id,
            'parent_id': self.parent_id,
            'level': self.level,
            'event_type': self.event_type,
            'message': self.message,
            'start_date': self.start_date,
            'end_date': self.end_date
        }
