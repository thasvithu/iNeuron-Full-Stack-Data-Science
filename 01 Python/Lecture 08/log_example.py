import logging

# Configure logging to show INFO and above
logging.basicConfig(level=logging.INFO)

logging.debug("This is a debug message")    # Won't show
logging.info("This is an info message")     # Will show
logging.warning("This is a warning")        # Will show


