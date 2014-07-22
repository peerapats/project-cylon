import pytest
import yaml

from project_cylon.Page import *
from project_cylon.Element import *

from project_cylon.PageFactory import *

class TestPageFactory:

    def test_create_page_return_page(self):
        content = open("./tests/GooglePage.yaml", "r")
        doc = yaml.load(content)

        page = PageFactory.create_page(doc)
        assert page.name == "google"
        assert page.url == "http://www.google.com"
        assert page.get_url("login") == "http://www.google.com/login"

        assert page.site_config['dev'] == "http://www.dev.google.com"
        assert page.site_config['default'] == "http://www.google.com"

        element = page.find_element("search input")
        assert element.name == "search input"
        assert element.identifier == "identifier"
