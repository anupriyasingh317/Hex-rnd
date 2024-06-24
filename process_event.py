import json
from events import Event
from src.db_handler import EventLogger

def process_event(event_data):
    event = Event(
        run_id=event_data.get('runId'),
        parent_id=event_data.get('parentId'),
        level=event_data.get('level'),
        event_type=event_data.get('EventType'),
        message=event_data.get('Message'),
        start_date=event_data.get('StartDate'),
        end_date=event_data.get('EndDate')
    )
    event_logger.log_event(event)

if __name__ == "__main__":
    # Initialize the EventLogger
    event_logger = EventLogger(
        # dbname='your_db_name',
        # user='your_db_user',
        # password='your_db_password',
        # host='your_db_host',
        # port=your_db_port

        # POSTGRES_DATABASE_URI="
        host='c-gen-ai-test-db.xyr2br6ljuwsr7.postgres.cosmos.azure.com' ,
        port=6432,
        dbname='rapidx' ,
        user='citus' ,
        password='Codescout123' ,
        sslmode='require',
        POSTGRES_CONN_STR='postgresql://rapidx:{password}@c-gen-ai-test-db.xyr2br6ljuwsr7.postgres.cosmos.azure.com:6432/rapidx?sslmode=require',
        POSTGRES_PWD='Codescout123',
    )

    # Example of event data from the queue
    event_data_1 = {
        "runId": 1,
        "parentId": 1,
        "level": "File",
        "EventType": "Parse",
        "Message": "Parse Completed",
        "StartDate": None,
        "EndDate": None
    }

    event_data_2 = {
        "runId": 1,
        "parentId": 1,
        "level": "Run",
        "EventType": "Run Completed",
        "Message": "Run Completed",
        "StartDate": None,
        "EndDate": None
    }

    # Process the events
    process_event(event_data_1)
    process_event(event_data_2)

    # Close the EventLogger connection
    event_logger.close()
