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
# FIXME test movement control

'''

import ffmpeg

packet_size = 4096

process = ffmpeg.input('rtsp://deuterio:D3uT33RR10@192.168.0.21:554/stream1').output('./.out/audio.mp4', format='mulaw').run_async(pipe_stdout=True)
packet = process.stdout.read(packet_size)

while process.poll() is None:
    packet = process.stdout.read(packet_size)
    print(packet)
'''

'''

friendly_name: “Move left”
command_on: ‘curl -k “http://xxx:xxx@192.168.1.41:8300/cgi-bin/hi3510/ptzctrl.cgi?-step=1&-act=left”’

friendly_name: “Move right”
command_on: ‘curl -k “http://xxx:xxx@192.168.1.41:8300/cgi-bin/hi3510/ptzctrl.cgi?-step=1&-act=right”’

friendly_name: “Move up”
command_on: ‘curl -k “http://xxx:xxx@192.168.1.41:8300/cgi-bin/hi3510/ptzctrl.cgi?-step=1&-act=up”’

friendly_name: “Move down”
command_on: ‘curl -k “http://xxx:xxx@192.168.1.41:8300/cgi-bin/hi3510/ptzctrl.cgi?-step=1&-act=down”’

friendly_name: “Home”
command_off: ‘curl -k “http://xxx:xxx@192.168.1.41:8300/cgi-bin/hi3510/ptzctrl.cgi?-step=1&-act=home

'''