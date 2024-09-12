from utils.Log import Log
from ActionExecutor import ActionExecutor
#from processors.audio_commander.AudioCommanderProcessor import AudioCommanderProcessor


if __name__ == '__main__2':
    Log.config()

    '''
    actions = ["ShowDetectionsProcessor", "VideoCameraClassImageSaverProcessor", "VideoCameraClassVideoSaverProcessor", 
               "ModelGenerator", "CameraMovementUI"]
    targets = ["LIGHTNINGS", "BIRDS",  "PEOPLE"]
    '''

    execute_action = "VideoCameraClassVideoSaverProcessor"
    target = "PEOPLE"
    ActionExecutor.execute(execute_action, target)


# FIXME test ffmpeg
'''
audio_commander_processor = AudioCommanderProcessor.from_config_file('config.properties')
audio_commander_processor.start_recording()
'''

import configparser


def get_rtsp_url(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    section = 'DEFAULT'

    user = config[section]['user']
    password = config[section]['password']
    host = config[section]['host']
    return f"rtsp://{user}:{password}@{host}:554/stream1"


# RTSP stream URL
rtsp_url = get_rtsp_url('config.properties')

#####################################################################################

import ffmpeg
import pyaudio
import wave
import speech_recognition as sr
import time
import threading

# Initialize PyAudio
p = pyaudio.PyAudio()

# Initialize recognizer
recognizer = sr.Recognizer()
rate = 16000
audio_format = pyaudio.paInt16


# Function to save audio chunks
def save_audio_chunk(chunk, filename):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(audio_format))
    wf.setframerate(rate)
    wf.writeframes(chunk)
    wf.close()


# Function to process audio chunks
def process_audio_chunk(audio_chunk):

    audio_data = sr.AudioData(audio_chunk, rate, p.get_sample_size(audio_format))

    try:
        text = recognizer.recognize_google(audio_data)
        print(f"Recognized Text: {text}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


# Function to capture audio from RTSP stream
def capture_audio(rtsp_url, chunk_size):
    process = (
        ffmpeg
        .input(rtsp_url)
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

        if len(audio_chunk) >= chunk_size:
            chunk_filename = f"./.out/audio_chunk_{chunk_count}.wav"
            chunk_count = chunk_count + 1
            save_audio_chunk(audio_chunk, chunk_filename)
            process_audio_chunk(audio_chunk)
            audio_chunk = b''


chunk_size = 16000 * 10  # 10 seconds

# Start capturing audio in a separate thread
audio_thread = threading.Thread(target=capture_audio, args=(rtsp_url, chunk_size))
audio_thread.start()

# Keep the main thread alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping audio capture...")


'''
I need to create a python code that can connect to a RTSP stream and send chunks of the audio data to the library SpeechRecognition so that I can obtain the text from the speech. I also need to use the function 'adjust_for_ambient_noise' from the recognizer to reduce the noise. I want also to save each chunk of audio in a file for later check. The chunks must be of 10 seconds'''