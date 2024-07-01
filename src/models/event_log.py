from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EventLog(Base):
    __tablename__ = 'event_logs'
    __table_args__ = {'schema':'codebits'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    run_id = Column(Integer, nullable=False)
    parent_id = Column(Integer)
    level = Column(String(50))
    event_type = Column(String(50))
    message = Column(Text)
    start_date = Column(TIMESTAMP)
    end_date = Column(TIMESTAMP)
