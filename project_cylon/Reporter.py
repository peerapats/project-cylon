# -*- coding: utf-8 -*-
import os
import glob

from xml.dom import minidom
from TestCase import *

class Reporter:
    def generate_reports(self, srcfiles, destination):
        if not os.path.exists(destination):
            os.makedirs(destination)

        for file in glob.glob(srcfiles):
            self.generate_report(file, destination)

    def generate_report(self, srcfile, destination):
        xmldoc = minidom.parse(srcfile)
        testsuite = xmldoc.getElementsByTagName('testsuite')[0]

        filepath, filename = os.path.split(srcfile)
        filename = filename.replace('TESTS-', '').replace('.xml', '')

        feature = testsuite.attributes['name'].value.replace(filename + '.', '')

        # print "testsuite: %s" % testsuite.attributes['name'].value
        # print "failed: %s" % testsuite.attributes['failures'].value
        # print "skipped: %s" % testsuite.attributes['skipped'].value
        # print "total: %s" % testsuite.attributes['tests'].value

        testcases = xmldoc.getElementsByTagName('testcase')
        scenarios = []

        for item in testcases :
            testcase = TestCase(item)
            scenario = testcase.render_scenario()
            scenarios.append(scenario)

        html = """
        <html>
        <head>
            <title>Test report</title>
            <link rel="stylesheet" href="http://localhost:8080/css/bootstrap.css"/>
        </head>
        <body>
            <br/>
            <div class="container">

            <div class="panel panel-default">
              <div class="panel-heading">
                <h3 class="panel-title">Feature: %s</h3>
              </div>
              <div class="panel-body">%s</div>
            </div>

            </div>
        </body>
        </html>
        """ % (feature, '\n'.join(scenarios))

        filepath, filename = os.path.split(srcfile)
        filename = filename.replace('.xml', '.html')
        htmlfile = os.path.join(destination, filename)

        f = open(htmlfile, 'w')
        f.write(html.encode('utf-8'))
        f.close()