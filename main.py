from utils.Log import Log
from ActionExecutor import ActionExecutor


if __name__ == '__main__':
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


import ffmpeg

rtsp_url = 'rtsp://xxx:xxx@192.168.0.21:554/stream1'
output_file = './.out/output_audio.wav'

print(f'Start...')

# Extract audio and save to file
(
    ffmpeg
    .input(rtsp_url)
    .output(output_file, format='wav', acodec='pcm_s16le', map='0:a')
    .run()
)

print(f'Audio saved to {output_file}')
