import wx
from camera_movement.CameraMovement import CameraMovement
import traceback


class CameraMovementUI(wx.Frame):

    button_height = 50
    button_width = 100

    @staticmethod
    def launch():
        app = wx.App()
        CameraMovementUI()
        app.MainLoop()

    def __init__(self):
        super().__init__(parent=None, title='Camera Control Pad')
        panel = wx.Panel(self)

        self.create_button_pad(panel)

        self.camera_movement = CameraMovement.from_config_file(config_file='config.properties')

        self.Show()

    def create_button_pad(self, panel):

        left_margin = 30
        up_margin = 30
        button_height = CameraMovementUI.button_height
        button_width = CameraMovementUI.button_width

        CameraMovementUI.build_button_with_action(panel, 'UP', (left_margin + button_width, up_margin), self.on_press_up)
        CameraMovementUI.build_button_with_action(panel, 'DOWN', (left_margin + button_width, up_margin + 2 * button_height), self.on_press_down)
        CameraMovementUI.build_button_with_action(panel, 'LEFT', (left_margin, up_margin + button_height), self.on_press_left)
        CameraMovementUI.build_button_with_action(panel, 'RIGHT', (left_margin + 2 * button_width, up_margin + button_height), self.on_press_right)
        CameraMovementUI.build_button_with_action(panel, 'HOME', (left_margin + button_width, up_margin + button_height), self.on_press_home)

    @staticmethod
    def build_button_with_action(panel, label, pos, action):
        my_btn = wx.Button(panel, label=label, pos=pos, size=(CameraMovementUI.button_width, CameraMovementUI.button_height))
        my_btn.Bind(wx.EVT_BUTTON, action)

    def on_press_up(self, event):
        try:
            self.camera_movement.move_up()
        except:
            print("Problem with command up")
            traceback.print_exc()

    def on_press_down(self, event):
        try:
            self.camera_movement.move_down()
        except:
            print("Problem with command down")
            traceback.print_exc()

    def on_press_left(self, event):
        try:
            self.camera_movement.move_left()
        except:
            print("Problem with command left")
            traceback.print_exc()

    def on_press_right(self, event):
        try:
            self.camera_movement.move_right()
        except:
            print("Problem with command right")
            traceback.print_exc()

    def on_press_home(self, event):
        try:
            self.camera_movement.move_home()
        except:
            print("Problem with command home")
            traceback.print_exc()
