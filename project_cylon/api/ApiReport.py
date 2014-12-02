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

            info['files'].append({ 'filename': filename, 'status': testsuite.status })

        return json.dumps(info)
