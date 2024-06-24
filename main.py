# main.py
from db_handler import DBHandler
from queue_subscriber import QueueSubscriber

if __name__ == "__main__":
    POSTGRES_CONN_STR = (
      "host=c-gen-ai-test-db.xyr2br6ljuwsr7.postgres.cosmos.azure.com"
        "port=6432 dbname='rapidx' user='Codescout123' password='Codescout123' sslmode='require'"
    )

    # Initialize DBHandler
    db_handler = DBHandler(POSTGRES_CONN_STR)

    # Initialize QueueSubscriber
    queue_name = 'test_queue'  # Replace with your actual queue name
    rabbitmq_host = 'localhost'  # Replace with your RabbitMQ host if it's not localhost
    subscriber = QueueSubscriber(queue_name, db_handler, rabbitmq_host)

    try:
        # Start consuming messages
        subscriber.start_consuming()
    except KeyboardInterrupt:
        # Close connections gracefully
        subscriber.close()
        db_handler.close()
