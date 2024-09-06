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

    def move_home(self):

        # Revisar y ver Absolute movement
        x_home = (self.X_MAX_CONTINUOUS + self.X_MIN_CONTINUOUS) / 2
        y_home = (self.Y_MAX_CONTINUOUS + self.Y_MIN_CONTINUOUS) / 2
        self.move_continuous(x_home, y_home)

    def move_up(self):
        step = self.get_step_up_down()
        self.move_relative(0, step)

    def move_down(self):
        step = self.get_step_up_down()
        self.move_relative(0, -step)

    def move_left(self):
        step = self.get_step_left_right()
        self.move_relative(-step, 0)

    def move_right(self):
        step = self.get_step_left_right()
        self.move_relative(step, 0)

    def get_step_up_down(self):
        return (self.Y_MAX_RELATIVE - self.Y_MIN_RELATIVE) / 20

    def get_step_left_right(self):
        return (self.X_MAX_RELATIVE - self.X_MIN_RELATIVE) / 20


