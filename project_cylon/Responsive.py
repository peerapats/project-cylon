# -*- coding: utf-8 -*-
import glob
import yaml

from Logger import Logger as log

class Responsive():

    browser_sizes = {}

    @classmethod
    def load_browser_sizes(cls, filename):
        content = open(filename, "r")
        doc = yaml.load(content)

        for item in doc['browser_sizes']:
            try:
                name = item['name']
                size = item['size']

                width = int(size.split('x')[0].strip())
                height = int(size.split('x')[1].strip())

                cls.browser_sizes[name] = {
                    'width': width,
                    'height': height
                }
            except:
                log.failed("Invalid responsive configuration, please check");

    @classmethod
    def get_browser_size(cls, name):
        if name in cls.browser_sizes:
            return cls.browser_sizes[name]
        else:
            log.failed("Not found responsive config '%s'" % name)
