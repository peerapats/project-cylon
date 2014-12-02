# -*- coding: utf-8 -*-
from xml.dom import minidom

class TestCase:
    testcase = None
    steps_status = "passed"
    scenario_type = "Scenario"

    def __init__(self, testcase):
        self.testcase = testcase
        self.steps_status = "passed"
        self.scenario_type = "scenario"

    @property
    def name(self):
        return self.testcase.attributes['name'].value

    @property
    def status(self):
        return self.testcase.attributes['status'].value

    @property
    def error(self):
        errors = self.testcase.getElementsByTagName('error')

        if len(errors) == 0:
            return ""
        else:
            return errors[0].firstChild.wholeText

    def get_steps_status(self, line, status):
        if "passed" in line:
            status = "passed"
        elif "failed" in line:
            status = "failed"
        elif "skipped" in line:
            status = "skipped"
        elif "undefined" in line:
            status = "undefined"

        return status

    def render_steps(self):
        output = self.testcase.getElementsByTagName('system-out')[0]
        contents = output.firstChild.wholeText.split('\n')

        steps = []
        status = "passed"
        capture = False

        for line in contents:
            if "Scenario:" in line:
                self.scenario_type = "Scenario"
                capture = True
                continue

            if "Scenario Outline:" in line:
                self.scenario_type = "Scenario Outline"
                capture = True
                continue

            if "scenario.end" in line:
                capture = False
                break

            if capture and line.strip() != "":
                status = self.get_steps_status(line, status)

                css_class = {
                    "passed": "text-success",
                    "failed": "text-danger",
                    "skipped": "text-info",
                    "undefined": "text-warning"
                }[status]

                steps.append('<div class="%s">%s</div>' % (css_class, line.strip()))

        return '\n'.join(steps)

    def render_error(self):
        error = []

        for line in self.error.split('\n'):
            if line.strip() == "":
                line = "<br>"
            error.append('<div>%s</div>' % line.strip())

        return '\n'.join(error[:-2])

    def render_scenario(self):
        css_class = {
            "passed":  "panel-success",
            "failed":  "panel-danger",
            "skipped": "panel-info"
        }[self.status]

        steps = self.render_steps()
        error = self.render_error()

        html = """
        <div class="panel %s">
            <div class="panel-heading">
                <h3 class="panel-title">%s: %s</h3>
            </div>
            <div class="panel-body">
            %s
            %s
            </div>
        </div>
        """ % (css_class, self.scenario_type, self.name, steps, error)

        return html
