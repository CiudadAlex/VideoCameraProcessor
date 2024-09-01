import time


class TimeRegulator:

    def __init__(self, interval_millis):
        self.interval_millis = interval_millis
        self.start = time.time()

    def wait_until_next_milestone(self):

        now = time.time()
        milliseconds_passed = now - self.start

        if milliseconds_passed >= self.interval_millis:
            # We are late. Do nothing
            pass
        else:

            millis_left = self.interval_millis - milliseconds_passed
            time.sleep(millis_left/1000)

        self.start = time.time()
