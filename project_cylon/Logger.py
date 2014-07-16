# -*- coding: utf-8 -*-

class Logger:

    capture_stdout = False

    @classmethod
    def warning(cls, message):
        print "WARN: %s\n" % message
        #if cls.capture_stdout: raise "(warning)"

    @classmethod
    def failed(cls, message, actual="--", expect="--"):
        details = message

        if actual != "--" and expect != "--":
            #details = "%s\nactual: '%s'\nexpect: '%s'\n" % (message, actual, expect)
            details = """
            %s
            actual: '%s'
            expect: '%s'
            """ % (message, actual, expect)

        print "FAIL: %s" % details

        #if cls.capture_stdout: raise "(failed)"
        raise "(stdout)"
