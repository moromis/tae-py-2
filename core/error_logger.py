import logging


logger = None


def log_error(error: Exception):
    global logger
    if logger == None:
        logging.basicConfig(
            filename="error.log",
            level=logging.ERROR,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
    logging.error(error)
