import logging.config

# Function to setup logging configuration from logger.ini
def setup_logging():
    logging.config.fileConfig('logger.ini', disable_existing_loggers=False)

def main():
    # Setup logging configuration
    setup_logging()

    # Get the logger for the current module
    logger = logging.getLogger(__name__)
    
    # Example logging messages
    logger.info('Application starting...')
    logger.warning('This is a warning message.')
    logger.error('An error occurred.')

    # Your application code here
    logger.info('Application finished.')

if __name__ == "__main__":
    main()
