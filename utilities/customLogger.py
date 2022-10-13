import logging
import sys


# noinspection SpellCheckingInspection
class LogGen:
    # noinspection SpellCheckingInspection
    logging.basicConfig(filename=".\\logs\\automation.log",
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
