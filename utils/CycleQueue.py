import threading


class CycleQueue:

    def __init__(self, max_size):
        self.q = []
        self.lock = threading.Lock()
        self.max_size = max_size
        self.original_max_size = max_size
        self.last_item = None

    def add(self, item):

        with self.lock:
            if len(self.q) >= self.max_size:
                del self.q[0]

            self.q.append(item)
            self.last_item = item

    def get_last_item(self):

        with self.lock:
            return self.get_last_item

    def get_all_and_reset(self):

        with self.lock:
            returned_list = self.q
            self.q = []
            self.max_size = self.original_max_size
            return returned_list

    def remove_limit_max_size(self):

        with self.lock:
            self.max_size = 1000000000
