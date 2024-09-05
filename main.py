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
# FIXME test movement control

'''

import ffmpeg

packet_size = 4096

process = ffmpeg.input('rtsp://xxxx:xxxx@192.168.0.21:554/stream1').output('./.out/audio.mp4', format='mulaw').run_async(pipe_stdout=True)
packet = process.stdout.read(packet_size)

while process.poll() is None:
    packet = process.stdout.read(packet_size)
    print(packet)
'''

import time
from onvif import ONVIFCamera
mycam = ONVIFCamera('192.168.0.21', 2020, 'deuterio', 'D3uT33RR10', './venv/Lib/site-packages/wsdl/')


# Create ptz service
ptz = mycam.create_ptz_service()
print(ptz)
media = mycam.create_media_service()

# Get target profile
media_profile = media.GetProfiles()[0]

# Get PTZ configuration options for getting continuous move range
request = ptz.create_type('GetConfigurationOptions')
configuration_token = media_profile.PTZConfiguration.token
request.ConfigurationToken = configuration_token
ptz_configuration_options = ptz.GetConfigurationOptions(configuration_token)

moverequest = ptz.create_type('ContinuousMove')
moverequest.ProfileToken = media_profile.token

"""
if moverequest.Velocity is None:
    moverequest.Velocity = ptz.GetStatus({'ProfileToken': media_profile.token}).Position
    moverequest.Velocity.PanTilt.space = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].URI
    moverequest.Velocity.Zoom.space = ptz_configuration_options.Spaces.ContinuousZoomVelocitySpace[0].URI
"""

# Get range of pan and tilt
XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min

print(str(XMIN) + " " + str(XMAX) + " " + str(YMIN) + " " + str(YMAX))

velocity = {
    "PanTilt": {
        "x": XMIN,
        "y": YMIN,
    },
}
moverequest.Velocity = velocity

time.sleep(2)

print ('move left...')
#request.Velocity.PanTilt.x = XMIN
#request.Velocity.PanTilt.y = 0

def do_move(ptz, request):
    # Start continuous move
    # ptz.Stop({'ProfileToken': request.ProfileToken})
    ptz.ContinuousMove(request)

do_move(ptz, moverequest)


