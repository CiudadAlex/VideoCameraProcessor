import configparser
import ffmpeg
import pyaudio
import wave
import speech_recognition as sr
import time
import threading
import queue


class AudioCommanderProcessor:

    def __init__(self, user, password, host):

        # Form RTSP URL
        self.rtsp_url = f"rtsp://{user}:{password}@{host}:554/stream1"

        # Initialize PyAudio
        self.p = pyaudio.PyAudio()

        # Initialize recognizer
        self.recognizer = sr.Recognizer()

        # Variables
        self.rate = 16000
        self.audio_format = pyaudio.paInt16
        self.chunk_size = self.rate * 10  # 10 seconds

        self.queue_of_chunks = queue.Queue()
        self.recognized_text = None

    @classmethod
    def from_config_file(cls, config_file):

        config = configparser.ConfigParser()
        config.read(config_file)

        section = 'DEFAULT'

        user = config[section]['user']
        password = config[section]['password']
        host = config[section]['host']
        return cls(user, password, host)

    # Function to save audio chunks
    def save_audio_chunk(self, chunk, filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.p.get_sample_size(self.audio_format))
        wf.setframerate(self.rate)
        wf.writeframes(chunk)
        wf.close()

    # Function to process audio chunks
    def process_audio_chunk(self, audio_chunk, function_with_recognized_text):

        audio_data = sr.AudioData(audio_chunk, self.rate, self.p.get_sample_size(self.audio_format))

        try:
            text = self.recognizer.recognize_google(audio_data)
            print(f"Recognized Text: {text}")

            if self.recognized_text is None:
                self.recognized_text = text
            else:
                self.recognized_text = self.recognized_text + " " + text

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            if self.recognized_text is not None:

                function_with_recognized_text(self.recognized_text)

                print("Back waiting for commands...")

                with self.queue_of_chunks.mutex:
                    self.queue_of_chunks.queue.clear()

            self.recognized_text = None

        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            self.recognized_text = None

    # Function to capture audio from RTSP stream
    def capture_audio(self, save_audio_files):
        process = (
            ffmpeg
            .input(self.rtsp_url)
            .output('pipe:', format='wav', acodec='pcm_s16le', ac=1, ar='16000')
            .run_async(pipe_stdout=True)
        )

        chunk_count = 0

        audio_chunk = b''
        while True:
            in_bytes = process.stdout.read(1024)
            if not in_bytes:
                break
            audio_chunk += in_bytes

            if len(audio_chunk) >= self.chunk_size:

                if save_audio_files:
                    chunk_filename = f"./.out/audio_chunk_{chunk_count}.wav"
                    chunk_count = chunk_count + 1
                    self.save_audio_chunk(audio_chunk, chunk_filename)

                self.queue_of_chunks.put(audio_chunk)

                audio_chunk = b''

    def start_recording(self, save_audio_files, function_with_recognized_text):

        print(f'Start...')

        # Start capturing audio in a separate thread
        audio_thread = threading.Thread(target=self.capture_audio, args=(save_audio_files,))
        audio_thread.start()

        # Keep the main thread alive
        try:
            while True:
                time.sleep(1)
                audio_chunk = self.queue_of_chunks.get()
                self.process_audio_chunk(audio_chunk, function_with_recognized_text)
                self.queue_of_chunks.task_done()

        except KeyboardInterrupt:
            print("Stopping audio capture...")

