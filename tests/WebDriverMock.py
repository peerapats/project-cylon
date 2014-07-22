from Mocker import *

from AlertMock import *
from WebElementMock import *

class WebDriverMock(Mocker):

    def __init__(self):
        super(WebDriverMock, self).__init__()

    @property
    def current_url(self):
        return self.call("current_url")

    @property
    def window_handles(self):
        return self.call("window_handles")

    def find_element_by_id(self, identifier):
        return self.call("find_element_by_id")

    def find_element_by_name(self, identifier):
        return self.call("find_element_by_name")

    def find_element_by_class_name(self, identifier):
        return self.call("find_element_by_class_name")

    def find_element_by_link_text(self, identifier):
        return self.call("find_element_by_link_text")

    def find_element_by_xpath(self, identifier):
        return self.call("find_element_by_xpath")

    def find_elements_by_xpath(self, identifier):
        return self.call("find_elements_by_xpath")

    def execute(self, command, target):
        self.call("execute")
        pass

    def execute_script(self, script, element):
        self.call("execute_script")
        pass

    def get(self, url):
        self.call("get")
        pass

    def switch_to_window(self, handle):
        self.call("switch_to_window")
        pass

    def switch_to_alert(self):
        return self.call("switch_to_alert")
