from utils.di_setup import setup_di
from kink import di
from services.queue_subscriber import QueueSubscriber

def main():
    setup_di()
    subscriber = di[QueueSubscriber]

    try:
        subscriber.run()
    except KeyboardInterrupt:
        subscriber.close()
        db_handler = di[DBHandler]
        db_handler.close()

if __name__ == "__main__":
    main()
