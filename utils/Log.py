import logging
import os


class Log:

    @staticmethod
    def config():

        path_log_file = "./.out/log.txt"

        if os.path.exists(path_log_file):
            os.remove(path_log_file)

        open(path_log_file, 'a').close()

        logging.basicConfig(filename=path_log_file,
                            force=True,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
