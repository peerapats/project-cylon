# -*- coding: utf-8 -*-
import os
import sys
import json
import glob
import shutil

import cherrypy
import subprocess

from Reporter import *


class TestServer(object):

    def __init__(self):
        self.project = os.getcwd()
        self.clear_reports()

        print "Running on dir: %s" % self.project

    @cherrypy.expose
    def index(self):
        filepath, filename = os.path.split(__file__)
        filename = os.path.join(filepath, "public", "test-runner.html")

        htmlfile = open(filename, 'r')
        return htmlfile.read()

    @cherrypy.expose
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
    def run(self, options="all"):
        self.clear_reports()
        subprocess.call("cd %s && cylon run %s junit" % (self.project, options), shell=True)
        self.generate_reports()

    @cherrypy.expose
    def reports(self):
        info = {
            'path': '/project/reports/html',
            'files': []
        }
        html_files = os.path.join(self.project, 'reports', 'html', '*.html')

        for file in glob.glob(html_files):
            filepath, filename = os.path.split(file)
            info['files'].append(filename)

        return json.dumps(info)

    @cherrypy.expose
    def clear_reports(self):
        path = os.path.join(self.project, 'reports')
        if os.path.exists(path):
            shutil.rmtree(path)

    def generate_reports(self):
        junit_files = os.path.join(self.project, 'reports', '*.xml')
        destination = os.path.join(self.project, 'reports', 'html')

        reporter = Reporter()
        reporter.generate_reports(junit_files, destination)

        return "html reports generated."
