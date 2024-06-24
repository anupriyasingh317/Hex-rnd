import pika
import json
from db_handler import DBHandler

class QueueSubscriber:
    def __init__(self, queue_name, db_handler, rabbitmq_url):
        self.queue_name = queue_name
        self.db_handler = db_handler
        self.rabbitmq_url = rabbitmq_url
        self.connection = None
        self.channel = None

    def connect(self):
        try:
            parameters = pika.URLParameters(self.rabbitmq_url)
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=self.queue_name, durable=True)
            print(f"Connected to RabbitMQ. Waiting for messages on '{self.queue_name}'")
        except Exception as e:
            print(f"Error connecting to RabbitMQ: {e}")
            raise

    def callback(self, ch, method, properties, body):
        try:
            print(f"Received message: {body.decode()}")
            event = json.loads(body)
            # Insert the event into the database
            self.db_handler.insert_event(event)
            # Acknowledge the message
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Error processing message: {e}")

    def start_consuming(self):
        try:
            self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=False)
            self.channel.start_consuming()
        except KeyboardInterrupt:
            print("Interrupted. Closing subscriber.")
        except Exception as e:
            print(f"Error consuming messages: {e}")
            raise
        finally:
            if self.connection and self.connection.is_open:
                self.connection.close()

    def run(self):
        try:
            self.connect()
            self.start_consuming()
        except Exception as e:
            print(f"Error running subscriber: {e}")
        finally:
            if self.connection and self.connection.is_open:
                self.connection.close()

# Example usage:
# if __name__ == "__main__":
#     # Replace with your RabbitMQ URL and queue name
#     rabbitmq_url = 'amqp://lxptmxtz:xuBCHtJkSOBnUUHYcI8hht9A3uw1G_Dy@puffin-01.rmq2.cloudamqp.com/lxptmxtz'
#     queue_name = 'my_queue'

#     # Replace with your PostgreSQL connection string
#     POSTGRES_CONN_STR = (
#         "host=c-gen-ai-test-db.xyr2br6ljuwsr7.postgres.cosmos.azure.com "
#         "port=6432 dbname=rapidx user=citus password=Codescout123 sslmode=require"
#     )

#     # Initialize DBHandler with PostgreSQL connection string
#     db_handler = DBHandler(POSTGRES_CONN_STR)

#     # Create QueueSubscriber instance
#     subscriber = QueueSubscriber(queue_name, db_handler, rabbitmq_url)

#     # Run the subscriber
#     subscriber.run()
