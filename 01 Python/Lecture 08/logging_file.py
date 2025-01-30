import logging

logging.basicConfig (
    filename="app.log",
    filemode="w",
    level=logging.DEBUG
)

logging.debug("This goes to the file")
logging.info("This too!")