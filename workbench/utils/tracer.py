from loguru import logger


def trace_time(func):
    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        res = func(*args, **kwargs)
        logger.debug(f"{func.__name__} took {time.time() - start} seconds")
        return res

    return wrapper