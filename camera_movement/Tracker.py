

class Traker:

    def __init__(self, width, height, camera_movement):
        self.width = width
        self.height = height
        self.camera_movement = camera_movement

    def track(self, rectangle_up_left_position, rectangle_down_right_position):
        x1 = rectangle_up_left_position[0]
        y1 = rectangle_up_left_position[1]
        x2 = rectangle_down_right_position[0]
        y2 = rectangle_down_right_position[1]

        left_margin = x1
        right_margin = self.width - x2
        up_margin = y1
        down_margin = self.height - y2

    # FIXME finish

