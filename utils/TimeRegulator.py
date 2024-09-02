import time


class TimeRegulator:

    def __init__(self, interval_millis):
        self.interval_millis = interval_millis
        self.start = time.time()
        self.start_check_freq = time.time()
        self.count_check_freq = 0

    def wait_until_next_milestone(self):

        now = time.time()
        seconds_passed = now - self.start
        milliseconds_passed = 1000 * seconds_passed

        if milliseconds_passed >= self.interval_millis:
            # We are late. Do nothing
            pass
        else:

            millis_left = self.interval_millis - milliseconds_passed
            time.sleep(millis_left/1000)

        self.start = time.time()
        self.check_freq()

    def check_freq(self):

        self.count_check_freq = self.count_check_freq + 1
        now = time.time()
        seconds_passed = now - self.start_check_freq

        if seconds_passed >= 1:
            freq = self.count_check_freq / seconds_passed
            print(">>>>> " + str(freq) + " per second")

            # Reset
            self.count_check_freq = 0
            self.start_check_freq = time.time()

