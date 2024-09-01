import threading


class CycleQueue:

    def __init__(self, max_size):
        self.q = []
        self.lock = threading.Lock()
        self.max_size = max_size
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

