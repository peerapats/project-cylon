# -*- coding: utf-8 -*-
import glob
import yaml

from Logger import Logger as log

class SiteConfig():

    config = {}

    @classmethod
    def get_site_config(cls, filename, site="default"):
        content = open(filename, 'r')
        doc = yaml.load(content)
        cls.config = doc['sites']

        if site == 'default':
            site = cls.config['default']

        if site not in cls.config:
            log.failed("Not found specified site name '%s'" % site)

        return cls.config[site]
