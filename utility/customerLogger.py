import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)


        return logger