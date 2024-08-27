import rtsp
import time


class RtspClient:

    def __init__(self, user, password, host):

        rtsp_url = f"rtsp://{user}:{password}@{host}:554/stream1"
        self.client = rtsp.Client(rtsp_server_uri=rtsp_url, verbose=True)

    def show_screen(self):

        time.sleep(2.5)
        self.client.read().show()

    def close(self):
        self.client.close()
