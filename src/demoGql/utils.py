import logging
from functools import wraps

# from contextlib import ContextDecorator

logging.basicConfig(level=logging.INFO)


# class dev_logger(ContextDecorator):
#     def __init__(self, name: str = 'default', **kwargs):
#         self.name = name
#         self.kwargs = kwargs
#
#     def __enter__(self):
#         params = {{k: v} for k, v in self.kwargs.items()}
#         logging.info(f'Entering: {self.name} with: params {params}')
#
#     def __exit__(self, exc_type, exc, exc_tb):
#         logging.info(f'Exiting: {self.name}')


def dev_log(function):
    logging.info(f'Entering: {function.__name__}', )

    @wraps(function)
    def wrapper(*args, **kwargs):
        logging.info(f'The positional in {function.__name__} arguments are: {args}', )
        logging.info(f'The keyword arguments in {function.__name__} are: {kwargs}', )
        logging.info(f'Exiting: {function.__name__}', )
        return function(*args, **kwargs)

    return wrapper
