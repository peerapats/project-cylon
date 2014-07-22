from Mocker import *

class WebElementMock(Mocker):

    def __init__(self):
        super(WebElementMock, self).__init__()

    @property
    def id(self):
        return self.call("id")

    @property
    def tag_name(self):
        return self.call("tag_name")

    def get_attribute(self, attribute):
        return self.call("get_attribute")

    def is_enabled(self):
        return self.call("is_enabled")

    def is_displayed(self):
        return self.call("is_displayed")

    def is_selected(self):
        return self.call("is_selected")

    def send_keys(self, value):
        self.call("send_keys")
        pass

    def click(self):
        self.call("click")
        pass

    def find_elements(self, by, identifier):
        return self.call("find_elements")
