import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)


def dev_log(function):
    logging.info(f'Entering: {function.__name__}', )

    @wraps(function)
    def wrapper(*args, **kwargs):
        logging.info(f'The positional in {function.__name__} arguments are: {args}', )
        logging.info(f'The keyword arguments in {function.__name__} are: {kwargs}', )
        logging.info(f'Exiting: {function.__name__}', )
        return function(*args, **kwargs)

    return wrapper
