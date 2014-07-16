import pytest

from WebDriverMock import *
from WebElementMock import *

from project_cylon.Element import *


class TestElement:

    def test_name_return_name(self):
        element = Element("name", "identifier")
        assert element.name == "name"

    def test_identifier_return_identifier(self):
        element = Element("name", "identifier")
        assert element.identifier == "identifier"

    def test_get_instance_return_element_instance(self):
        driver = WebDriverMock()

        element = Element("xpath", "input")
        element.driver = driver

        instance = WebElementMock()
        instance.tag_name = "input"

        assert element.get_instance() == instance

    def test_get_instance_return_None(self):
        driver = WebDriverMock()

        element = Element("link_text", None)
        element.driver = driver

        assert element.get_instance() == None

    def test_get_instances_return_element_list(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        element1 = WebElementMock()
        element2 = WebElementMock()

        elements = []
        elements.append(element1)
        elements.append(element2)

        assert element.get_instances() == elements

    def test_input_value_return_value_from_value(self):
        driver = WebDriverMock()

        element = Element("xpath", "input")
        element.driver = driver

        assert element.value == "value from @value"

    def test_select_value_return_value_from_select(self):
        driver = WebDriverMock()

        element = Element("xpath", "select")
        element.driver = driver

        assert element.value == "value from @value"

    def test_div_value_return_value_from_innerHTML(self):
        driver = WebDriverMock()

        element = Element("xpath", "div")
        element.driver = driver

        assert element.value == "value from @innerHTML"

    # def test_None_element_value_return_empty_value(self):
    #     driver = WebDriverMock()
    #
    #     element = Element("id", None)
    #     element.driver = driver
    #
    #     assert element.value == ""

    def test_tooltip_text_return_tooltip_text(self):
        driver = WebDriverMock()

        element = Element("name", "tootip")
        element.driver = driver

        assert element.title == "value from @title"

    def test_exists_return_True(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        assert element.exists == True

    def test_enabled_return_True(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        assert element.enabled == True

    def test_visible_return_True(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        assert element.visible == True

    def test_selected_return_True(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        assert element.selected == True

    def test_count_return_2(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        assert element.count == 2

    def test_send_keys_return_True(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        assert element.send_keys("keystroke") == True

    def test_send_keys_by_script_return_True(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        assert element.send_keys_by_script("keystroke") == True

    def test_click_return_True(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        assert element.click() == True

    def test_select_return_True(self):
        driver = WebDriverMock()

        element = Element("xpath", "select")
        element.driver = driver

        assert element.select("option") == True

    def test_check_return_True(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        assert element.check() == True

    def test_uncheck_return_True(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        assert element.uncheck() == True

    def test_mouse_move_over_return_True(self):
        driver = WebDriverMock()

        element = Element()
        element.driver = driver

        assert element.move_mouse_over() == True
