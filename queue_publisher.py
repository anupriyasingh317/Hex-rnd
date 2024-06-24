import pika
import json

# RabbitMQ connection parameters
credentials = pika.PlainCredentials('lxptmxtz', 'xuBCHtJkSOBnUUHYcI8hht9A3uw1G_Dy')
parameters = pika.ConnectionParameters(
    host='puffin-01.rmq2.cloudamqp.com',
    port=5672,
    virtual_host='lxptmxtz',
    credentials=credentials,
    ssl_options=None
)

# Establish connection
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare queue
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name, durable=True)

# Sample messages
sample_messages = [
    {"runId": 1, "parentId": 1, "level": "Test", "EventType": "Check", "Message": "Check Completed"},
    # {"runId": 1, "parentId": 1, "level": "Test", "EventType": "process Completed", "Message": "process Completed"}
]

# Publish messages to the queue
for message in sample_messages:
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
    print(f"Sent message: {message}")

# Close connection
connection.close()
