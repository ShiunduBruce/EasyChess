import logging

# Handles logging features to make debugging easier
class Logger:

    __slots__ = ('ch', 'fh', 'logger', 'formatter')

    def __init__(self, file_handler):
        self.ch = logging.StreamHandler()
        self.fh = logging.FileHandler('{}'.format(file_handler))
        self.logger = logging.getLogger('easychess')
        self.formatter = logging.Formatter('%(asctime)s - %(message)s')

    def overwrite_logging(self, handling, file_name):
        with open('{}'.format(file_name), handling):
            pass

        self.logger.setLevel(logging.DEBUG)
        self.fh.setLevel(logging.DEBUG)
        self.ch.setLevel(logging.ERROR)
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def info(self, text):
        self.logger.info(text)

    def warning(self, text):
        self.logger.warning(text)

