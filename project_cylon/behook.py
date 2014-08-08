#!/usr/bin/env python

from behave import configuration
from behave import __main__

## add my wanted option to parser.
configuration.parser.add_argument('--browser', help="Specify browser to run, firefox or chrome")
configuration.parser.add_argument('--site', help="Specify site to run")

## command that run behave.
def main():
    return __main__.main()
