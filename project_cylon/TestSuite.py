# -*- coding: utf-8 -*-
from xml.dom import minidom

class TestSuite:

    def __init__(self, doc):
        self.testsuite = doc.getElementsByTagName('testsuite')[0]

    @property
    def name(self):
        return self.testsuite.attributes['name'].value

    @property
    def tests(self):
        return int(self.testsuite.attributes['tests'].value)

    @property
    def errors(self):
        return int(self.testsuite.attributes['errors'].value)

    @property
    def skipped(self):
        return int(self.testsuite.attributes['skipped'].value)

    @property
    def failures(self):
        return int(self.testsuite.attributes['failures'].value)

    @property
    def time(self):
        return float(self.testsuite.attributes['time'].value)

    @property
    def failed(self):
        return self.failures + self.errors

    @property
    def passed(self):
        return self.tests - self.failed - self.skipped

    @property
    def status(self):
        if self.failed > 0:
            return "failed"
        elif self.passed > 0:
            return "passed"
        else:
            return "skipped"
