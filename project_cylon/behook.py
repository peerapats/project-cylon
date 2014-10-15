#!/usr/bin/env python

from behave import configuration
from behave import __main__

## add my wanted option to parser.
configuration.parser.add_argument('--browser')
configuration.parser.add_argument('--site')
configuration.parser.add_argument('--debug', action='store_true')
configuration.parser.add_argument('--screenshot', action='store_true')

## command that run behave.
def main():
    return __main__.main()
