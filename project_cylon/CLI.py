#!/usr/bin/env python

import os
import sys
import textwrap

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

        ## create settings.yaml
        content = get_settings_content()
        new_file(directory, "settings.yaml", textwrap.dedent(content))

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
    target = "./features"

    ## update environment.py
    content = get_environment_content()
    update_file(target, "environment.py", textwrap.dedent(content))

###
### command: cylon run ...
###
def run_all():
    print "Running all features..."
    os.system("behave --color --quiet --no-skipped")

def run_tags(tags):
    print "Running with tags: %s" % tags

    argtags = ""
    for tag in tags:
        argtags = "%s --tags=%s" % (argtags, tag)

    os.system("behave --color --quiet --no-skipped %s" % argtags.strip())

###
### print instruction
###
def print_instruction():
    content = get_instruction()
    print content

###
### get content functions
###
def get_settings_content():
    content = """
    ### Default project settings ###
    ---
    #
    # Browser to run test (!now support only firefox).
    #
    RUN_ON_BROWSER: firefox

    #
    # Switch page URL to the specified site.
    # To use this option you need to add "site_url:" section in your page object.
    #
    SITE_URL: default
    ...
    """
    return content

def get_accounts_content():
    content = """
    ### Define user accounts to use with login keyword ###
    ---
    accounts:

    - name: pcms admin
      username: test@domain.com
      password: 123456
    ...
    """

def get_steps_content():
    content = """
    ###
    ### Implement additional step definitions here.
    ###
    """
    return content

def get_environment_content():
    content = """
    from selenium import webdriver
    from project_cylon.PageFactory import *
    from project_cylon.CommonSteps import *
    from project_cylon.World import World as world

    def before_all(context):
        world.driver = webdriver.Firefox()
        world.pages = PageFactory.create_pages("./pageobjects/*.yaml", world.driver, "default")

    def after_all(context):
        for handle in world.driver.window_handles:
            world.driver.switch_to_window(handle)
            world.driver.close()
    """
    return content

# def get_environment_content():
#     content = """
#     import sys
#     import yaml
#
#     from project_cylon.WorldContext import *
#     from project_cylon.CommonSteps import *
#
#     content = open("./settings.yaml", "r")
#     settings = yaml.load(content)
#
#     def before_all(context):
#         World.OpenBrowser(settings['RUN_ON_BROWSER'])
#         World.LoadPageObjects("./pageobjects/*.yaml", settings['SITE_URL'])
#         #World.LoadAccounts("accounts.yaml")
#
#     def after_all(context):
#         World.CloseBrowser()
#     """
#     return content

def get_shell_runall_content():
    content = """
    #!/bin/bash
    echo "Running all features..."
    behave --quiet --no-skipped
    """
    return content

# def get_shell_runtags_content():
#     content = """
#     #!/bin/bash
#
#     echo -n "Please specify tags to run >> "
#     read tags
#     echo "Running with tags: $tags"
#
#     behave --quiet --no-skipped --tags=$tags
#     """
#     return content

def get_batch_runall_content():
    content = """
    @echo off
    echo "Running all features..."
    behave --color --quiet --no-skipped
    pause
    """
    return content

# def get_batch_runtags_content():
#     content = """
#     """
#     return content

def get_instruction():
    content = """
    Usage:
    cylon <command> [arguments]

    Commands:
    new project <name>                Create new project directory.
    new feature <name>                Create new feature file.
    new pageobject <name>             Create new pageobject file.

    update project                    Update project files to compatible
                                      with current version.

    run all                           Run test with all feature.
    run tags <tags>                   Run test with specified tags.
    """
    return content

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
                run_all()
            elif sub == "tags":
                tags = sys.argv[3:]
                run_tags(tags)
        elif command == "update":
            sub = sys.argv[2].lower()

            if sub == "project":
                update_project()

    except: print_instruction()
