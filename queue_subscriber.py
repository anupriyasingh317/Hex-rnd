# queue_subscriber.py
import pika
import json
from db_handler import DBHandler

class QueueSubscriber:
    def __init__(self, queue_name, db_handler, rabbitmq_host='localhost'):
        self.queue_name = queue_name
        self.db_handler = db_handler
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def callback(self, ch, method, properties, body):
        print(f"Received {body}")
        event = json.loads(body)
        # Insert the event into the database
        self.db_handler.insert_event(event)
        # Acknowledge the message
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=False)
        print('Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def close(self):
        self.connection.close()
