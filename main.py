from db_handler import DBHandler
from queue_subscriber import QueueSubscriber

if __name__ == "__main__":
    POSTGRES_CONN_STR = (
        "host=c-gen-ai-test-db.xyr2br6ljuwsr7.postgres.cosmos.azure.com "
        "port=6432 dbname='rapidx' user='citus' password='Codescout123' sslmode='require'"
    )

    # Initialize DBHandler
    db_handler = DBHandler(POSTGRES_CONN_STR)

    # Initialize QueueSubscriber
    queue_name = 'my_queue'  # Replace with your actual queue name
    rabbitmq_url = 'amqps://lxptmxtz:xuBCHtJkSOBnUUHYcI8hht9A3uw1G_Dy@puffin-01.rmq2.cloudamqp.com/lxptmxtz'

    subscriber = QueueSubscriber(queue_name, db_handler, rabbitmq_url)

    try:
        # Start consuming messages
        subscriber.run()
    except KeyboardInterrupt:
        # Close connections gracefully
        subscriber.close()
        db_handler.close()
