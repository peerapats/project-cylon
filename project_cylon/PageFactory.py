# -*- coding: utf-8 -*-
import glob
import yaml

from Page import *
from Element import *

from Logger import Logger as log

class PageFactory:

    @classmethod
    def create_page(cls, doc, driver):
        page = Page(doc['page']['name'], doc['page']['url'])
        page.driver = driver

        if "url_paths" in doc['page']:
            for item in doc['page']['url_paths']:
                name = item['name']
                path = item['path']

                if not name in page.url_paths:
                    page.url_paths[name] = path
                else:
                    log.warning("%s\nDuplicate url path name: '%s'" % (page.name, name))

        if "elements" in doc:
            for item in doc['elements']:
                element = Element(item['name'], item['xpath'])
                element.driver = page.driver

                if not element.name in page.elements:
                    page.elements[element.name] = element
                else:
                    log.warning("%s\nDuplicate element name: '%s'" % (page.name, element.name))

        if "site_url" in doc:
            page.site_config = doc['site_url']
            page.site_config['default'] = page.url

        return page

    @classmethod
    def create_pages(cls, path, driver, site):
        pages = {}

        for filename in glob.glob(path):
            content = open(filename, "r")
            docs = yaml.load_all(content)

            for doc in docs:
                page = cls.create_page(doc, driver)
                page.switch_site(site)

                if not page.name in pages:
                    pages[page.name] = page
                else:
                    log.failed("Duplicate page name: '%s'" % page.name)

        return pages
