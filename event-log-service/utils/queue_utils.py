# queue_utils.py
import pika
import os
from dotenv import load_dotenv
load_dotenv() 

url = os.environ.get('RABBITMQ_URL')
connection = pika.BlockingConnection(pika.URLParameters(url))
channel = connection.channel()

def bind_consumer(queue):
    def bind(consumer):
        channel.queue_declare(queue=queue, durable=True)
        channel.basic_consume(queue=queue, on_message_callback=consumer)
    return bind
