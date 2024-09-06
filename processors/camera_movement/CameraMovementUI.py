import wx


class CameraMovementUI(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='Camera Control Pad')
        panel = wx.Panel(self)

        CameraMovementUI.build_button_with_action(panel, 'UP', (55, 5), self.on_press_up)
        CameraMovementUI.build_button_with_action(panel, 'DOWN', (55, 100), self.on_press_down)
        CameraMovementUI.build_button_with_action(panel, 'LEFT', (5, 55), self.on_press_left)
        CameraMovementUI.build_button_with_action(panel, 'RIGHT', (100, 55), self.on_press_right)

        self.Show()

    @staticmethod
    def build_button_with_action(panel, label, pos, action):
        my_btn = wx.Button(panel, label=label, pos=pos)
        my_btn.Bind(wx.EVT_BUTTON, action)

    def on_press_up(self, event):
        print("up")

    def on_press_down(self, event):
        print("down")

    def on_press_left(self, event):
        print("left")

    def on_press_right(self, event):
        print("right")

