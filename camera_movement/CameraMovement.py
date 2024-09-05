import time
from onvif import ONVIFCamera
import configparser


class CameraMovement:

    def __init__(self, user, password, host):
        self.my_cam = ONVIFCamera(host, 2020, user, password, './venv/Lib/site-packages/wsdl/')

        # Create ptz service
        self.ptz = self.my_cam.create_ptz_service()
        self.media = self.my_cam.create_media_service()

        # Get target profile
        self.media_profile = self.media.GetProfiles()[0]

        configuration_token = self.media_profile.PTZConfiguration.token
        ptz_configuration_options = self.ptz.GetConfigurationOptions(configuration_token)

        # Get range of pan and tilt
        self.X_MAX_CONTINUOUS = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
        self.X_MIN_CONTINUOUS = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
        self.Y_MAX_CONTINUOUS = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
        self.Y_MIN_CONTINUOUS = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min

        self.X_MAX_RELATIVE = ptz_configuration_options.Spaces.RelativePanTiltTranslationSpace[0].XRange.Max
        self.X_MIN_RELATIVE = ptz_configuration_options.Spaces.RelativePanTiltTranslationSpace[0].XRange.Min
        self.Y_MAX_RELATIVE = ptz_configuration_options.Spaces.RelativePanTiltTranslationSpace[0].YRange.Max
        self.Y_MIN_RELATIVE = ptz_configuration_options.Spaces.RelativePanTiltTranslationSpace[0].YRange.Min

        time.sleep(2)

    @classmethod
    def from_config_file(cls, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)

        section = 'DEFAULT'

        user = config[section]['user']
        password = config[section]['password']
        host = config[section]['host']
        return cls(user, password, host)

    def move_continuous(self, x, y):

        move_request = self.ptz.create_type('ContinuousMove')
        move_request.ProfileToken = self.media_profile.token

        velocity = {
            "PanTilt": {
                "x": x,
                "y": y,
            },
        }
        move_request.Velocity = velocity
        self.ptz.ContinuousMove(move_request)

    def move_relative(self, x, y):

        move_request = self.ptz.create_type('RelativeMove')
        move_request.ProfileToken = self.media_profile.token

        translation = {
            "PanTilt": {
                "x": x,
                "y": y,
            },
        }
        move_request.Translation = translation
        self.ptz.RelativeMove(move_request)

    # FIXME pulir. En mover relativo que sean porcentajes de min-max

    def move_min(self):
        self.move_continuous(self.X_MIN_CONTINUOUS, self.X_MIN_CONTINUOUS)

    def move_max(self):
        self.move_continuous(self.X_MAX_RELATIVE, self.X_MAX_RELATIVE)

    def move_a_bit(self):
        self.move_relative(0.1, 0.1)

