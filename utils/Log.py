import logging


class Log:

    @staticmethod
    def config():
        logging.basicConfig(filename="./.out/log.txt",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
