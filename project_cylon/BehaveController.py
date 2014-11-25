# -*- coding: utf-8 -*-
from Logger import *
from Responsive import *

from SiteConfig import *
from PageFactory import *
from CommonSteps import *

from World import World as world


class BehaveController:

    @classmethod
    def before_all(cls, context):
        Logger.tracebacklimit(0)
        if context.config.debug == True:
            Logger.tracebacklimit(1000)

        if context.config.screenshot == True:
            Logger.enable_screenshots()

        ## load responsive config
        Responsive.load_browser_sizes("./responsive.yaml")

        ## load site config
        site = "default"
        if hasattr(context.config, "site") and context.config.site is not None:
            site = context.config.site

        SiteConfig.load_config("./config.yaml", site)
        world.urls = SiteConfig.get_urls()
        world.variables = SiteConfig.get_variables()

        ## load page objects
        pageobjects = "./pageobjects/*.yaml"
        if PageFactory.check_yaml_syntax(pageobjects) == True:
            world.pages = PageFactory.create_pages(pageobjects)
        else:
            Logger.failed("Stop running.")


    @classmethod
    def after_all(cls, context):
        pass


    @classmethod
    def before_feature(cls, context, feature):
        if hasattr(context.config, "browser_size") and context.config.browser_size is not None:
            name = context.config.browser_size
            size = Responsive.get_browser_size(name)
            world.size = size

        ## setup browser
        browser = "firefox"
        if hasattr(context.config, "browser") and context.config.browser is not None:
            browser = context.config.browser

        world.open_browser(browser)
        Logger.driver = world.driver


    @classmethod
    def after_feature(cls, context, feature):
        world.close_browser()
