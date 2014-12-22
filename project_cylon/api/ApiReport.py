# -*- coding: utf-8 -*-
import os
import glob
import json
import cherrypy

from xml.dom import minidom

from ..TestSuite import *


class ApiReport(object):

    def __init__(self):
        self.project = os.getcwd()

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def info(self):
        info = {
            'path': '/project/reports/html',
            'files': []
        }

        xml_files = os.path.join(self.project, 'reports', '*.xml')

        for file in glob.glob(xml_files):
            xmldoc = minidom.parse(file)
            testsuite = TestSuite(xmldoc)

            filepath, filename = os.path.split(file)
            filename = filename.replace('.xml', '.html')

            item = {
                'filename': filename,
                'status': testsuite.status,
                'passed': testsuite.passed,
                'failed': testsuite.failed,
                'total': testsuite.tests,
                'duration': testsuite.time
            }

            info['files'].append(item)

            #info['files'].append({ 'filename': filename, 'status': testsuite.status })

        return json.dumps(info)

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def mock_info(self):
        info = {
            'path': '/project/reports/html',
            'files': [
                {
                    'filename:': 'report-passed.html',
                    'status': 'passed',
                    'passed': 12,
                    'failed': 3,
                    'total': 15,
                    'duration': 10.1234
                },
                {
                    'filename': 'report-failed.html',
                    'status': 'failed',
                    'passed': 12,
                    'failed': 3,
                    'total': 15,
                    'duration': 10.1234
                },
                {
                    'filename': 'report-skipped.html',
                    'passed': 12,
                    'failed': 3,
                    'total': 15,
                    'duration': 10.1234
                }
            ]
        }
        return json.dumps(info)
