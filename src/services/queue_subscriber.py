import pika
import json
from models.db_handler_interface import DBHandlerInterface
from kink import inject

@inject
class QueueSubscriber:
    def __init__(self, queue_name: str, db_handler: DBHandlerInterface, rabbitmq_url: str):
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
            self.db_handler.insert_event(event)
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
