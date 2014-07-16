
class WebElementMock:

    id = ""
    tag_name = ""

    def __init__(self):
        self.id = ""
        self.tag_name = ""

    def __eq__(self, other):
        return self.id == other.id and self.tag_name == other.tag_name

    def find_elements(self, by, identifier):
        option1 = WebElementMock()
        option2 = WebElementMock()

        options = []
        options.append(option1)
        options.append(option2)

        return options

    def get_attribute(self, attribute):
        return "value from @%s" % attribute

    def is_enabled(self):
        return True

    def is_displayed(self):
        return True

    def is_selected(self):
        return True

    def send_keys(self, value):
        pass

    def click(self):
        pass
