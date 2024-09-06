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
'''
from camera_movement.CameraMovement import CameraMovement

camera_movement = CameraMovement.from_config_file(config_file='config.properties')
camera_movement.move_a_bit()
'''


import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        my_btn = wx.Button(panel, label='Press Me', pos=(5, 55))
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()



