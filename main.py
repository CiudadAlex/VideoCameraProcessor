from utils.Log import Log
from ActionExecutor import ActionExecutor


if __name__ == '__main__2':
    Log.config()

    '''
    actions = ["ShowDetectionsProcessor", "VideoCameraClassImageSaverProcessor", "VideoCameraClassVideoSaverProcessor", "ModelGenerator"]
    targets = ["LIGHTNINGS", "BIRDS",  "PEOPLE"]
    '''

    execute_action = "ModelGenerator"
    target = "LIGHTNINGS"
    ActionExecutor.execute(execute_action, target)


# FIXME test ffmpeg
# FIXME tracking processor

'''

import ffmpeg

packet_size = 4096

process = ffmpeg.input('rtsp://xxxx:xxxx@192.168.0.21:554/stream1').output('./.out/audio.mp4', format='mulaw').run_async(pipe_stdout=True)
packet = process.stdout.read(packet_size)

while process.poll() is None:
    packet = process.stdout.read(packet_size)
    print(packet)
'''

from camera_movement.CameraMovement import CameraMovement

camera_movement = CameraMovement.from_config_file(config_file='config.properties')
camera_movement.move_a_bit()

