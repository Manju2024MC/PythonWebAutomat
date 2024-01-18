import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("This is the information log")
    LOGGER.warning("This is the warning logs")
    LOGGER.error("this is the error logs")
    LOGGER.critical("this is the critical logs")