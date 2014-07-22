# -*- coding: utf-8 -*-
import sys

class Logger:

    @classmethod
    def tracebacklimit(cls, value=1000):
        sys.tracebacklimit = int(value)

    @classmethod
    def warning(cls, message, fields={}):
        message = "WARN: %s\n" % message

        for key, value in fields.iteritems():
            message += "  %s: '%s'\n" % (key, value)

        print message
        raise RuntimeError

    @classmethod
    def failed(cls, message, actual="--", expect="--"):
        message = "FAIL: %s\n" % message

        if actual != "--" and expect != "--":
            message += "actual: '%s'\nexpect: '%s'\n" % (actual, expect)

        print message
        raise RuntimeError
