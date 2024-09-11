import configparser
import ffmpeg


class AudioCommanderProcessor:

    def __init__(self, user, password, host):

        self.rtsp_url = f"rtsp://{user}:{password}@{host}:554/stream1"
        self.output_file = './.out/output_audio.wav'

    @classmethod
    def from_config_file(cls, config_file):

        config = configparser.ConfigParser()
        config.read(config_file)

        section = 'DEFAULT'

        user = config[section]['user']
        password = config[section]['password']
        host = config[section]['host']
        return cls(user, password, host)

    def start_recording(self):
        print(f'Start...')

        # Extract audio and save to file
        (
            ffmpeg
            .input(self.rtsp_url)
            .output(self.output_file, format='wav', acodec='pcm_s16le', map='0:a')
            .run()
        )

        print(f'Audio saved to {self.output_file}')

