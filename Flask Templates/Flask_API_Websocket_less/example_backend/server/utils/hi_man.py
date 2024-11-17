
class HiMan:
    def __init__(self, callback):
        self.callback = callback
        self.response = "Hi man !"

    def send_hi(self):
        self.callback(self.response)

    def modify_talk(self, sentence):
        self.response = sentence
