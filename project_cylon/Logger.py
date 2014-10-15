# -*- coding: utf-8 -*-
import os
import sys
import shutil

class Logger:

    driver = None

    screenshot_path = "./screenshots"
    screenshot_number = 1
    screenshot_enabled = False

    @classmethod
    def enable_screenshots(cls):
        cls.screenshot_enabled = True

        if os.path.exists(cls.screenshot_path):
            shutil.rmtree(cls.screenshot_path)

        os.makedirs(cls.screenshot_path)

    @classmethod
    def tracebacklimit(cls, value=0):
        sys.tracebacklimit = int(value)

    @classmethod
    def warning(cls, message, fields={}):
        message = "WARN: %s\n" % message

        for key, value in fields.iteritems():
            message += "  %s: '%s'\n" % (key, value)

        print message
        raise RuntimeError

    @classmethod
    def failed(cls, message, actual="", expect=""):
        message = "FAIL: %s\n" % message

        if actual != "" and expect != "":
            message += "actual: '%s'\nexpect: '%s'\n" % (actual, expect)

        print message

        if cls.screenshot_enabled == True:
            filename = "%s/%03d.png" % (cls.screenshot_path, cls.screenshot_number)
            cls.driver.save_screenshot(filename)
            cls.screenshot_number += 1

            print "Save screenshot to '%s'" % filename

        raise RuntimeError
