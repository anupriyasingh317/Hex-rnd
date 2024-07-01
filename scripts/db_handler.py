# db_handler.py
import psycopg2

class DBHandler:
    def __init__(self, conn_str):
        self.conn_str = conn_str
        self.connection = psycopg2.connect(conn_str)
        self.cursor = self.connection.cursor()

    def insert_event(self, event):
        query = """
            INSERT INTO event_logs (run_id, parent_id, level, event_type, message, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (
            event['runId'],
            event['parentId'],
            event['level'],
            event['EventType'],
            event['Message'],
            event.get('StartDate'),
            event.get('EndDate')
        ))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
