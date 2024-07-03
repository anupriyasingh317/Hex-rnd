from typing import Optional
from sqlalchemy import Column, String, INTEGER, TEXT, TIMESTAMP
from .base import Base


class Eventlogs(Base):
    __tablename__ = 'event_logs'
    __table_args__ = {'schema':'codebits'}

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    run_id = Column(INTEGER, nullable=False)
    parent_id = Column(INTEGER)
    level = Column(String(50))
    event_type = Column(String(50))
    message = Column(TEXT)
    start_date = Column(TIMESTAMP)
    end_date = Column(TIMESTAMP)

    def __init__(
                self,
                run_id: int,
                parent_id: int,
                level: str,
                event_type: str,
                message: TEXT,
                start_date: str,
                end_date: str
        ):
            self.run_id = run_id
            self.parent_id = parent_id
            self.level = level
            self.event_type = event_type
            self.message = message
            self.start_date = start_date
            self.end_date = end_date