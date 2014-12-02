# -*- coding: utf-8 -*-
import os
import shutil
import cherrypy
import subprocess

from ..Reporter import *

class ApiRun(object):

    def __init__(self):
        self.project = os.getcwd()

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def start(self, options="all"):
        path = os.path.join(self.project, 'reports')
        reporter = Reporter(path)
        reporter.clear_reports()

        subprocess.call("cd %s && cylon run %s junit" % (self.project, options), shell=True)
        reporter.generate_reports()

    def generate_reports(self):
        path = os.path.join(self.project, 'reports')
        reporter = Reporter(path)
        reporter.generate_reports()

    def clear_reports(self):
        path = os.path.join(self.project, 'reports')
        reporter = Reporter(path)
        reporter.clear_reports()
