import wx


class CameraMovementUI(wx.Frame):

    button_height = 50
    button_width = 100

    def __init__(self):
        super().__init__(parent=None, title='Camera Control Pad')
        panel = wx.Panel(self)

        self.create_button_pad(panel)

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

    @staticmethod
    def build_button_with_action(panel, label, pos, action):
        my_btn = wx.Button(panel, label=label, pos=pos, size=(CameraMovementUI.button_width, CameraMovementUI.button_height))
        my_btn.Bind(wx.EVT_BUTTON, action)

    def on_press_up(self, event):
        print("up")

    def on_press_down(self, event):
        print("down")

    def on_press_left(self, event):
        print("left")

    def on_press_right(self, event):
        print("right")

