# -*- coding: utf-8 -*-
import os
import glob
import json
import cherrypy

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
        html_files = os.path.join(self.project, 'reports', 'html', '*.html')

        for file in glob.glob(html_files):
            filepath, filename = os.path.split(file)
            info['files'].append(filename)

        return json.dumps(info)
