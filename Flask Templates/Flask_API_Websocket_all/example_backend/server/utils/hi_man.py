
class HiMan:
    def __init__(self, callback):
        self.callback = callback

    def send_hi(self):
        response = "Hi man !"
        self.callback(response)
