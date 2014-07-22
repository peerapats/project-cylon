from Mocker import *

class AlertMock(Mocker):

    def __init__(self):
        super(AlertMock, self).__init__()

    @property
    def text(self):
        return self.call("text")

    def accept(self):
        self.call("accept")
        pass

    def dismiss(self):
        self.call("dismiss")
        pass

    def send_keys(self):
        self.call("send_keys")
        pass
