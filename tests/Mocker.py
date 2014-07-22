
class Mocker(object):

    def __init__(self):
        self._called = {}
        self._expected = {}

    def expect(self, name, value):
        self._expected[name] = value

    def call(self, name):
        if name not in self._called:
            self._called[name] = 1
        else:
            self._called[name] += 1

        if name in self._expected:
            return self._expected[name]
        else:
            return None

    def called(self, name):
        if name in self._called:
            return self._called[name]
        else:
            return 0
