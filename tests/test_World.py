import pytest

from WebDriverMock import *
from WebElementMock import *

from project_cylon.Page import *
from project_cylon.Element import *
from project_cylon.PageFactory import *

from project_cylon.World import World as world


class TestWorld:

    def test_find_page_return_Page(self):
        world.pages = PageFactory.create_pages("./tests/*.yaml", "default")

        page = world.find_page("google")
        assert page.name == "google"

    def test_find_element_by_name_return_Element(self):
        world.pages = PageFactory.create_pages("./tests/*.yaml", "default")

        element = world.find_element("search input")
        assert element.name == "search input"
        assert element.identifier == "identifier"

    def test_find_element_without_name_return_Element(self):
        world.pages = PageFactory.create_pages("./tests/*.yaml", "default")

        element = world.find_element("q")
        assert element.name == "!!undefined"
        assert element.identifier == "q"

    def test_alert_return_Alert(self):
        instance = AlertMock()
        instance.expect("text", "alert message!!")

        driver = WebDriverMock()
        driver.expect("switch_to_alert", instance)

        world.driver = driver

        alert = world.get_alert()
        assert alert.text == "alert message!!"
