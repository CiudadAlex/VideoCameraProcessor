import logging
import os


class Log:

    @staticmethod
    def config():

        path_log_file = "./.out/log.txt"
        os.remove(path_log_file)

        logging.basicConfig(filename=path_log_file,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
