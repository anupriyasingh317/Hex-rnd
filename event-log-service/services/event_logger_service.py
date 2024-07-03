# services/event_logger_service.py
from kink import inject, di
from repo.event_logger_repository import EventLoggerRepository

@inject
class EventLoggerService:

    def process_event(self, event_message):
        # Assuming event_message is a dict
        di[EventLoggerRepository].insert_events(event_message)
