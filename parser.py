# parser.py
import time
from events import Event
from src.db_handler import EventLogger

event_logger = EventLogger("bolt://localhost:7687", "neo4j", "password")

def trigger_file_parse_event(file_name):
    timestamp = time.time()
    event = Event(timestamp, "Parser", "FileParseEvent", f"File: {file_name} parsed")
    event_logger.log_event(event)

# Other logic related to Parser service
