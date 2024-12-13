import logging

logging.basicConfig(
    filename="logfile.log", format="%(asctime)s %(message)s", filemode="w"
)

# Creating an object and setting to DEBUG
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
