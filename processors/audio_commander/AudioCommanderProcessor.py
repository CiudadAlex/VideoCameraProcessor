import configparser
import ffmpeg
import time


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
        process = (
            ffmpeg
            .input(self.rtsp_url)
            .output(self.output_file, format='wav', acodec='pcm_s16le', map='0:a')
            .run_async(pipe_stdout=True)
        )

        time.sleep(20)
        process.stdout.close()
        time.sleep(1)
        process.terminate()
        print(f'Audio saved to {self.output_file}')

        # I need to create a python code that can connect to a RTSP stream  and store the audio in a file
        # instead of saving it to an audio file, how can I send it to the library SpeechRecognition so that I can obtain the text from the speech

'''
import ffmpeg
import pyaudio
import speech_recognition as sr

# RTSP stream URL
rtsp_url = 'rtsp://your_rtsp_stream_url'

# Audio format settings
audio_format = pyaudio.paInt16
channels = 1
rate = 44100
chunk = 1024

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open a stream to save audio
stream = p.open(format=audio_format,
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=chunk)

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from RTSP stream
process = (
    ffmpeg
    .input(rtsp_url)
    .output('pipe:', format='wav')
    .run_async(pipe_stdout=True)
)

print("Recording... Press Ctrl+C to stop.")

try:
    while True:
        data = process.stdout.read(chunk)
        if not data:
            break
        audio_data = sr.AudioData(data, rate, p.get_sample_size(audio_format))
        try:
            text = recognizer.recognize_google(audio_data)
            print("Recognized Text: ", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
except KeyboardInterrupt:
    print("Recording stopped.")
    process.terminate()

# Close everything
stream.stop_stream()
stream.close()
p.terminate()
process.stdout.close()

'''
