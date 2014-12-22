# -*- coding: utf-8 -*-
import os
import cherrypy

class TestServer(object):

    def __init__(self):
        self.project = os.getcwd()
        print "Running on dir: %s" % self.project

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def index(self):
        filepath, filename = os.path.split(__file__)
        filename = os.path.join(filepath, "public", "test-runner-new.html")

        htmlfile = open(filename, 'r')
        return htmlfile.read()
