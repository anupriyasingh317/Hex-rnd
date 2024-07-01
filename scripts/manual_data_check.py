# manual_data_processor.py
import json
from db_handler import DBHandler

def process_manual_data(db_handler, data):
    try:
        event = json.loads(data)
        db_handler.insert_event(event)
        print(f"Processed and inserted event: {event}")
    except Exception as e:
        print(f"Failed to process data: {data} with error: {e}")

if __name__ == "__main__":
    POSTGRES_CONN_STR = (
        "host=c-gen-ai-test-db.xyr2br6ljuwsr7.postgres.cosmos.azure.com "
        "port=6432 dbname='rapidx' user='citus' password='Codescout123' sslmode='require'"
    )

    # Initialize DBHandler
    db_handler = DBHandler(POSTGRES_CONN_STR)

    # Sample data to simulate manual queue messages
    manual_data = [
        '{"runId": 1, "parentId": 1, "level": "File", "EventType": "Parse", "Message": "Parse Completed", "StartDate": null, "EndDate": null}',
        '{"runId": 1, "parentId": 1, "level": "Run", "EventType": "Run Completed", "Message": "Run Completed", "StartDate": null, "EndDate": null}'
    ]

    for data in manual_data:
        process_manual_data(db_handler, data)

    # Close the database handler
    db_handler.close()
