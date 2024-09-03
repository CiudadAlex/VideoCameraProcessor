from utils.Log import Log
from ActionExecutor import ActionExecutor


if __name__ == '__main__':
    Log.config()

    '''
    actions = ["ShowDetectionsProcessor", "VideoCameraClassImageSaverProcessor", "VideoCameraClassVideoSaverProcessor", "ModelGenerator"]
    targets = ["LIGHTNINGS", "BIRDS",  "PEOPLE"]
    '''

    execute_action = "ShowDetectionsProcessor"
    target = "LIGHTNINGS"
    ActionExecutor.execute(execute_action, target)


# FIXME test XSaverProcessors and ModelGenerator
# FIXME test ffmpeg

'''

import ffmpeg

packet_size = 4096

process = ffmpeg.input('rtsp://deuterio:D3uT33RR10@192.168.0.21:554/stream1').output('./.out/audio.mp4', format='mulaw').run_async(pipe_stdout=True)
packet = process.stdout.read(packet_size)

while process.poll() is None:
    packet = process.stdout.read(packet_size)
    print(packet)
'''