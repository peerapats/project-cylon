#!/usr/bin/env python
import os
import sys
import textwrap

import subprocess
import cherrypy

from TestServer import *

from api.ApiRun import *
from api.ApiReport import *
from api.ApiProject import *

###
### command: cylon new ...
###
def new_project(directory):
    if os.path.exists(directory):
        print "Directory is already exists."
        return True
    else:
        os.makedirs(directory)
        os.makedirs("%s/pageobjects" % directory)
        os.makedirs("%s/features/steps" % directory)

        ## create config.yaml
        content = get_config_content()
        new_file(directory, "config.yaml", textwrap.dedent(content))

        ## create responsive.yaml
        content = get_responsive_content()
        new_file(directory, "responsive.yaml", textwrap.dedent(content))

        ## create environment.py
        content = get_environment_content()
        new_file("%s/features" % directory, "environment.py", textwrap.dedent(content))

        ## create steps.py
        content = get_steps_content()
        new_file("%s/features/steps" % directory, "steps.py", textwrap.dedent(content))

        ## create runall.sh
        content = get_shell_runall_content()
        new_file(directory, "runall.sh", textwrap.dedent(content))

        ## create runall.bat
        content = get_batch_runall_content()
        new_file(directory, "runall.bat", textwrap.dedent(content))

        abs_path = os.path.abspath(directory)
        print  "New project created in: %s" % abs_path


def new_feature(filename):
    target = "./features"

    if not ".feature" in filename:
        filename = "%s.feature" % filename

    content = """
    @feature_tag
    Feature: Your feature description.

    @scenario_tag
    Scenario: Your scenario description.
    	Given your test preparation
    	When you do any action
    	Then you can verification
    """

    new_file(target, filename, textwrap.dedent(content))

def new_pageobject(filename):
    target = "./pageobjects"

    if not ".yaml" in filename:
        filename = "%s.yaml" % filename

    content = """
    --- ## %s
    page:
      name: %s
      url: http://yoursite.com

    elements:
    - name: title
      xpath: /html/head/title
    """ % (filename, filename.replace(".yaml", ""))

    new_file(target, filename, textwrap.dedent(content))

def new_file(target, filename, content=""):
    if not os.path.exists(target):
        print "Not found %s directory." % target
        return True

    if os.path.exists("%s/%s" % (target, filename)):
        print "File is already exists."
        return True

    new_file = open("%s/%s" % (target, filename), 'w')
    new_file.write(content)
    new_file.close()

    abs_path = os.path.abspath(target)
    print '%s created in: "%s".' % (filename, abs_path)

def update_file(target, filename, content=""):
    new_file = open("%s/%s" % (target, filename), 'w')
    new_file.write(content)
    new_file.close()

    abs_path = os.path.abspath(target)
    print '%s updated in: "%s".' % (filename, abs_path)

###
### command: cylon update ...
###
def update_project():
    ## update config.yaml
    if not os.path.exists("./config.yaml"):
        content = get_config_content()
        update_file("./", "config.yaml", textwrap.dedent(content))

    ## update responsive.yaml
    if not os.path.exists("./responsive.yaml"):
        content = get_responsive_content()
        update_file("./", "responsive.yaml", textwrap.dedent(content))

    ## update environment.py
    content = get_environment_content()
    update_file("./features", "environment.py", textwrap.dedent(content))

###
### command: cylon run ...
###
def get_options_string(options):
    command = ""

    for option in options:
        if "=" in option:
            name = option.split('=')[0].strip()
            value = option.split('=')[1].strip()
            option = '--%s="%s"' % (name, value)
        else:
            option = '--%s' % option
        command = "%s %s" % (command, option)

    return command

def run_shell(command, options=""):
    return subprocess.call("%s %s" % (command, options), shell=True)

###
### print instruction
###
def print_instruction():
    content = get_instruction()
    print content

###
### get content functions
###
def get_responsive_content():
    content = """
    ---
    browser_sizes:
    - name: my device
      size: 360 x 640
    ...
    """
    return content

def get_config_content():
    content = """
    --- ## site configurations
    site_config:
      default: develop

      develop:
        urls:
          web: http://dev.yourdomain.com
          mobile: http://m-dev.yourdomain.com
        variables:
          var1: dev

      production:
        urls:
          web: http://www.yourdomain.com
          mobile: http://m.yourdomain.com
        variables:
          var1: prod
          var2: 5678
    ...
    """
    return content

def get_steps_content():
    content = """
    ###
    ### Implement additional step definitions here.
    ###
    """
    return content

def get_environment_content():
    content = """
    from project_cylon.BehaveController import *

    def before_all(context):
        BehaveController.before_all(context)

    def before_feature(context, feature):
        BehaveController.before_feature(context, feature)

    def after_feature(context, feature):
        BehaveController.after_feature(context, feature)
    """
    return content

# def get_environment_content():
#     content = """
#     from project_cylon.Logger import *
#     from project_cylon.PageFactory import *
#     from project_cylon.CommonSteps import *

#     from project_cylon.World import World as world

#     def before_all(context):
#         Logger.tracebacklimit(0)
#         if context.config.debug == True:
#             Logger.tracebacklimit(1000)

#         if context.config.screenshot == True:
#             Logger.enable_screenshots()

#         site = "default"
#         if hasattr(context.config, "site") and context.config.site is not None:
#             site = context.config.site

#         domain = PageFactory.get_domain("./config.yaml", site)

#         pageobjects = "./pageobjects/*.yaml"
#         if PageFactory.check_yaml_syntax(pageobjects) == True:
#             world.pages = PageFactory.create_pages(pageobjects, domain)
#         else:
#             Logger.failed("Stop running.")

#     def before_feature(context, feature):
#         browser = "firefox"
#         if hasattr(context.config, "browser") and context.config.browser is not None:
#             browser = context.config.browser
#         world.open_browser(browser)

#         Logger.driver = world.driver

#     def after_feature(context, feature):
#         world.close_browser()
#     """
#     return content

def get_shell_runall_content():
    content = """
    #!/bin/bash
    echo "Running all features..."
    cylon run all
    """
    return content

def get_batch_runall_content():
    content = """
    @echo off
    echo "Running all features..."
    cylon run all
    pause
    """
    return content

def get_instruction():
    content = """
    Usage:
    cylon <command> [options]

    Commands:
    version                           Check project-cylon version.

    new project <name>                Create new project directory.
    new feature <name>                Create new feature file.
    new pageobject <name>             Create new pageobject file.

    update project                    Update project files to compatible
                                      with current version.

    run all                           Run test with all feature.
    run [options]                     Run with specified options.

    Options:
    tags=<tags>                       Set tags to run.
    site=<site>                       Set site to run (see config.yaml).
    browser-size=<name>               Set browser size to run (see responsive.yaml).
    debug                             Set to run in debug mode (show all traceback).
    """
    return content

def get_server_config():
    project_dir = os.getcwd()

    filepath, filename = os.path.split(__file__)
    public_dir = os.path.join(filepath, "public")

    config = {
        '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(public_dir, "css")
        },
        '/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(public_dir, "js")
        },
        '/project': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(project_dir)
        }
    }
    return config

###
### start script
###
def main():
    try:
        command = sys.argv[1].lower()

        if command == "new":
            sub = sys.argv[2].lower()
            filename = sys.argv[3]

            if sub == "project":
                new_project(filename)
            elif sub == "feature":
                new_feature(filename)
            elif sub in ["page", "pageobject"]:
                new_pageobject(filename)

        elif command == "run":
            sub = sys.argv[2].lower()

            if sub == "all":
                args = sys.argv[3:]
            else:
                args = sys.argv[2:]

            options = get_options_string(args)
            print args
            return run_shell("behook --color --quiet --no-skipped", options)

        elif command == "update":
            sub = sys.argv[2].lower()

            if sub == "project":
                update_project()

        elif command == "version":
            return run_shell("pip freeze | grep project-cylon")

        # elif command == "server":
        #     config = get_server_config()
        #     cherrypy.tree.mount(TestServer(), '/', config)

        #     cherrypy.tree.mount(ApiRun(), '/api/run')
        #     cherrypy.tree.mount(ApiReport(), '/api/report')
        #     cherrypy.tree.mount(ApiProject(), '/api/project')

        #     cherrypy.engine.start()
        #     cherrypy.engine.block()

    except: print_instruction()
