from loguru import logger


def validate_run_options(**kwargs):
    logger.debug(f"validate {kwargs}")
    if kwargs.get("molecule"):
        return True
    else:
        return False
