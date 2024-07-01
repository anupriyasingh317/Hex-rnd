from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.db_handler_interface import DBHandlerInterface
from models.event_log import Base, EventLog

class DBHandler(DBHandlerInterface):
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def insert_event(self, event):
        new_event = EventLog(
            run_id=event['runId'],
            parent_id=event['parentId'],
            level=event['level'],
            event_type=event['EventType'],
            message=event['Message'],
            start_date=event.get('StartDate'),
            end_date=event.get('EndDate')
        )
        self.session.add(new_event)
        self.session.commit()

    def close(self):
        self.session.close()

    def create_table(self):
        Base.metadata.create_all(self.engine)
