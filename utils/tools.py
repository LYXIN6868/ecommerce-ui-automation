import time


class Tools:
    def gettime(self):
        return time.strftime("%Y%m%d%H%M%S", time.localtime())
