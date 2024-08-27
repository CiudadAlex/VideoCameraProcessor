import rtsp
import time
import configparser


class RtspClient:

    def __init__(self, user, password, host):

        rtsp_url = f"rtsp://{user}:{password}@{host}:554/stream1"
        self.client = rtsp.Client(rtsp_server_uri=rtsp_url, verbose=True)

    @classmethod
    def from_config_file(cls, config_file):

        config = configparser.ConfigParser()
        config.read(config_file)

        section = 'DEFAULT'

        user = config[section]['user']
        password = config[section]['password']
        host = config[section]['host']
        return cls(user, password, host)

    def show_screen(self):

        time.sleep(2.5)
        self.client.read().show()

    def close(self):
        self.client.close()
