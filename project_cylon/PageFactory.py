# -*- coding: utf-8 -*-
import glob
import yaml

from yaml.parser import *
from yaml.scanner import *

from Page import *
from Element import *

from Logger import Logger as log

class PageFactory:

    @classmethod
    def check_yaml_syntax(cls, path):
        print "Checking yaml syntax..."

        error_files = 0

        for filename in glob.glob(path):
            content = open(filename, "r")
            docs = yaml.load_all(content)

            index = filename.rfind('/') + 1
            filename = filename[index:]

            try:
                for doc in docs: pass

            except ScannerError as exc:
                error_files += 1
                if hasattr(exc, 'problem_mark'):
                    mark = exc.problem_mark
                    print '  syntax error: file "%s", line %s' % (filename, mark.line)

            except ParserError as exc:
                error_files += 1
                if hasattr(exc, 'problem_mark'):
                    mark = exc.problem_mark
                    print '  syntax error: file "%s", line %s' % (filename, mark.line+1)

        if error_files == 0:
            print "  all file(s) passed."
            return True
        else:
            print "  found %s error file(s)." % error_files
            return False

    @classmethod
    def create_page(cls, doc):
        page = Page(doc['page']['name'], doc['page']['url'])
        #page.driver = driver

        if "url_paths" in doc['page']:
            for item in doc['page']['url_paths']:
                name = item['name']
                path = item['path']

                if not name in page.url_paths:
                    page.url_paths[name] = path
                else:
                    #log.warning("%s\nDuplicate url path name: '%s'" % (page.name, name))
                    log.warning("Duplicate url path name!", {
                        'page': page.name,
                        'path': name
                    })

        if "elements" in doc:
            for item in doc['elements']:
                element = Element(item['name'], item['xpath'])
                element.driver = page.driver

                if not element.name in page.elements:
                    page.elements[element.name] = element
                else:
                    #log.warning("%s\nDuplicate element name: '%s'" % (page.name, element.name))
                    log.warning("Duplicate element name!", {
                        'page': page.name,
                        'element': element.name
                    })

        if "site_url" in doc:
            page.site_config = doc['site_url']
            page.site_config['default'] = page.url

        return page

    @classmethod
    def create_pages(cls, path, site):
        pages = {}

        for filename in glob.glob(path):
            content = open(filename, "r")
            docs = yaml.load_all(content)

            for doc in docs:
                page = cls.create_page(doc)
                page.switch_site(site)

                if not page.name in pages:
                    pages[page.name] = page
                else:
                    #log.failed("Duplicate page name: '%s'" % page.name)
                    log.warning("Duplicate page name!", {
                        'page': page.name
                    })

        return pages
