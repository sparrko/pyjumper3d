import time

class Timer(object):
    def __init__(self):
        self.time = time.time()

    def getMilliseconds(self):
        return (time.time() - self.time) * 1000

    def restart(self):
        self.time = time.time()