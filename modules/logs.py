import logging

class Logger:
    def __init__(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        formatter = logging.Formatter('\033[93m[%(asctime)s %(levelname)s]\033[0m \033[94m%(message)s\033[0m')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        self.logger = logger

        self.f  = open('./data/log.txt', 'w')
        self.f.write('')

    def log(self, message: str, level = logging.INFO, dontCensor: bool = False):
        self.f  = open('./data/log.txt', 'a')
        self.f.write(message + '\n')

        if dontCensor == False: message = message.replace('\n', ' [\\n] ')
        if len(message) > 128 and dontCensor == False: message = "".join(message[slice(0, 128)] + "...")
        if level == logging.INFO: self.logger.info(message)
        if level == logging.ERROR: self.logger.error(message)
        