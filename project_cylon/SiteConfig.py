# -*- coding: utf-8 -*-
import glob
import yaml

from Logger import Logger as log

class SiteConfig():

    site = ""
    site_config = {}

    global_config = {}

    @classmethod
    def load_config(cls, filename, site="default"):
        content = open(filename, 'r')
        doc = yaml.load(content)

        if 'global_config' in doc:
            cls.global_config = doc['global_config']

        if 'site_config' in doc:
            cls.site_config = doc['site_config']

            if site == 'default':
                cls.site = cls.site_config['default']
            else:
                cls.site = site

        if cls.site not in cls.site_config:
            log.failed("Not found specified site name '%s'" % cls.site)

    @classmethod
    def get_urls(cls):
        urls = {}

        if 'urls' in cls.site_config[cls.site]:
            urls = cls.site_config[cls.site]['urls']

        return urls

    @classmethod
    def get_variables(cls):
        variables = {}

        if 'variables' in cls.global_config:
            variables = cls.global_config['variables']

        if 'variables' in cls.site_config[cls.site]:
            site_variables = cls.site_config[cls.site]['variables']
            for name in site_variables:
                variables[name] = site_variables[name]

        return variables
