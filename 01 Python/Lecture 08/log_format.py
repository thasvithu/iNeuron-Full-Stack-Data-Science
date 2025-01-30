import logging

logging.basicConfig(
    format="%(asctime)s -%(levelname)s -%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)

logging.info("Hello, logging!")