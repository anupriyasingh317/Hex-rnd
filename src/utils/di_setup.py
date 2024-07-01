import yaml
from kink import di
from repo.db_handler import DBHandler
from services.queue_subscriber import QueueSubscriber

def setup_di():
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    postgres_url = config['postgres']['url']
    rabbitmq_url = config['rabbitmq']['url']
    queue_name = config['rabbitmq']['queue_name']

    di[DBHandler] = DBHandler(postgres_url)
    db_handler = di[DBHandler]
    db_handler.create_table()

    di[QueueSubscriber] = QueueSubscriber(queue_name, db_handler, rabbitmq_url)
