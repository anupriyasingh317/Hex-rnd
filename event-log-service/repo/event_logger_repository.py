from kink import inject
from utils.postgres_utils import get_session
from models.postgres.event_logs import Eventlogs

@inject
class EventLoggerRepository():
    def insert_events(self, event_logs):
        with get_session() as session:
            new_event = Eventlogs(
                run_id=event_logs['run_id'],
                parent_id=event_logs['parent_id'],
                level=event_logs['level'],
                event_type=event_logs['event_type'],
                message=event_logs['message'],
                start_date=event_logs['start_date'],
                end_date=event_logs['end_date']
            )
            session.add(new_event)
            session.commit()

