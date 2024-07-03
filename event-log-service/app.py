# app.py
from dotenv import load_dotenv
load_dotenv()

import logging.config
import os
import sys
from kink import di
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from utils.queue_utils import bind_consumer, channel, connection
from services.event_logger_service import EventLoggerService
from utils.utils import get_logging_config
import json

from models.postgres.base import Base
from utils.postgres_utils import engine

Base.metadata.create_all(bind=engine)


# Setup logging
config_file_path = get_logging_config()
logging.config.fileConfig(config_file_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

@bind_consumer(queue=os.environ.get('EVENT_LOG_QUEUE_NAME'))
def consume_event_log_queue(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    try:
        event_message = json.loads(body)
        di[EventLoggerService].process_event(event_message)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

def main():

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        connection.close()

if __name__ == "__main__":
    main()
