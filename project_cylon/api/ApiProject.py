# -*- coding: utf-8 -*-
import os
import glob
import json
import cherrypy

class ApiProject(object):

    def __init__(self):
        self.project = os.getcwd()

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def info(self):
        info = {
            'project': 'undefined',
            'features': [],
            'page_objects': []
        }
        info['project'] = self.project

        path = os.path.join(self.project, "features", "*.feature")

        for file in glob.glob(path):
            dirname, filename = os.path.split(file)
            info['features'].append(filename)

        path = os.path.join(self.project, "pageobjects", "*.yaml")

        for file in glob.glob(path):
            dirname, filename = os.path.split(file)
            info['page_objects'].append(filename)

        return json.dumps(info)

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def load_config(self, configfile):
        content = configfile.file.read()
        return content
