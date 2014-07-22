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

    def test_get_instance_return_instance_by_xpath(self):
        instance = WebElementMock()
        instance.expect("tag_name", "input")

        driver = WebDriverMock()
        driver.expect("find_element_by_xpath", instance)

        element = Element("name", "identifier")
        element.driver = driver

        assert element.get_instance().tag_name == instance.tag_name

    def test_get_instance_return_instance_by_id(self):
        instance = WebElementMock()
        instance.expect("tag_name", "input")

        driver = WebDriverMock()
        driver.expect("find_element_by_id", instance)

        element = Element(identifier="identifier")
        element.driver = driver

        assert element.get_instance().tag_name == instance.tag_name

    def test_get_instance_return_None(self):
        driver = WebDriverMock()

        element = Element(identifier="identifier")
        element.driver = driver

        assert element.get_instance() == None

    def test_get_instances_return_element_list(self):
        elements = []
        elements.append(WebElementMock())
        elements.append(WebElementMock())

        driver = WebDriverMock()
        driver.expect("find_elements_by_xpath", elements)

        element = Element("name", "identifier")
        element.driver = driver

        assert element.get_instances() == elements

    def test_input_value_return_value_from_value(self):
        instance = WebElementMock()
        instance.expect("tag_name", "input")
        instance.expect("get_attribute", "@value")

        driver = WebDriverMock()
        driver.expect("find_element_by_id", instance)

        element = Element(identifier="identifier")
        element.driver = driver

        assert element.value == "@value"

    def test_div_value_return_value_from_innerHTML(self):
        instance = WebElementMock()
        instance.expect("tag_name", "div")
        instance.expect("get_attribute", "@innerHTML")

        driver = WebDriverMock()
        driver.expect("find_element_by_xpath", instance)

        element = Element("name", "identifier")
        element.driver = driver

        assert element.value == "@innerHTML"

    def test_tooltip_text_return_tooltip_text(self):
        instance = WebElementMock()
        instance.expect("get_attribute", "@title")

        driver = WebDriverMock()
        driver.expect("find_element_by_name", instance)

        element = Element(identifier="identifier")
        element.driver = driver

        assert element.title == "@title"

    def test_exists_return_True(self):
        instance = WebElementMock()

        driver = WebDriverMock()
        driver.expect("find_element_by_class_name", instance)

        element = Element()
        element.driver = driver

        assert element.exists == True

    def test_exists_return_False(self):
        driver = WebDriverMock()
        driver.expect("find_element_by_class_name", None)

        element = Element()
        element.driver = driver

        assert element.exists == False

    def test_enabled_return_True(self):
        instance = WebElementMock()
        instance.expect("is_enabled", True)

        driver = WebDriverMock()
        driver.expect("find_element_by_link_text", instance)

        element = Element()
        element.driver = driver

        assert element.enabled == True

    def test_enabled_return_False(self):
        instance = WebElementMock()
        instance.expect("is_enabled", False)

        driver = WebDriverMock()
        driver.expect("find_element_by_link_text", instance)

        element = Element()
        element.driver = driver

        assert element.enabled == False

    def test_visible_return_True(self):
        instance = WebElementMock()
        instance.expect("is_displayed", True)

        driver = WebDriverMock()
        driver.expect("find_element_by_name", instance)

        element = Element()
        element.driver = driver

        assert element.visible == True

    def test_visible_return_False(self):
        instance = WebElementMock()
        instance.expect("is_displayed", False)

        driver = WebDriverMock()
        driver.expect("find_element_by_name", instance)

        element = Element()
        element.driver = driver

        assert element.visible == False

    def test_selected_return_True(self):
        instance = WebElementMock()
        instance.expect("is_selected", True)

        driver = WebDriverMock()
        driver.expect("find_element_by_id", instance)

        element = Element()
        element.driver = driver

        assert element.selected == True

    def test_selected_return_False(self):
        instance = WebElementMock()
        instance.expect("is_selected", False)

        driver = WebDriverMock()
        driver.expect("find_element_by_id", instance)

        element = Element()
        element.driver = driver

        assert element.selected == False

    def test_count_return_2(self):
        elements = []
        elements.append(WebElementMock())
        elements.append(WebElementMock())

        driver = WebDriverMock()
        driver.expect("find_elements_by_xpath", elements)

        element = Element("name", "identifier")
        element.driver = driver

        assert element.count == 2

    def test_send_keys_return_True(self):
        instance = WebElementMock()

        driver = WebDriverMock()
        driver.expect("find_element_by_xpath", instance)

        element = Element("name", "identifier")
        element.driver = driver

        assert element.send_keys("keystroke") == True
        assert instance.called("send_keys") == 1

    def test_send_keys_by_script_return_True(self):
        instance = WebElementMock()

        driver = WebDriverMock()
        driver.expect("find_element_by_xpath", instance)

        element = Element("name", "identifier")
        element.driver = driver

        assert element.send_keys_by_script("keystroke") == True
        assert element.driver.called("execute_script") == 1

    def test_click_return_True(self):
        instance = WebElementMock()

        driver = WebDriverMock()
        driver.expect("find_element_by_xpath", instance)

        element = Element("name", "identifier")
        element.driver = driver

        assert element.click() == True
        assert instance.called("click") == 1

    def test_select_return_True(self):
        options = []
        options.append(WebElementMock())
        options.append(WebElementMock())

        instance = WebElementMock()
        instance.expect("tag_name", "select")
        instance.expect("find_elements", options)

        driver = WebDriverMock()
        driver.expect("find_element_by_xpath", instance)

        element = Element("name", "identifier")
        element.driver = driver

        assert element.select("option") == True

    def test_check_return_True(self):
        instance = WebElementMock()
        instance.expect("is_selected", False)

        driver = WebDriverMock()
        driver.expect("find_element_by_xpath", instance)

        element = Element("name", "identifier")
        element.driver = driver

        assert element.check() == True
        assert instance.called("is_selected") == 1
        assert instance.called("click") == 1

    def test_uncheck_return_True(self):
        instance = WebElementMock()
        instance.expect("is_selected", False)

        driver = WebDriverMock()
        driver.expect("find_element_by_xpath", instance)

        element = Element("name", "identifier")
        element.driver = driver

        assert element.uncheck() == True
        assert instance.called("is_selected") == 1
        assert instance.called("click") == 0

    def test_mouse_move_over_return_True(self):
        instance = WebElementMock()

        driver = WebDriverMock()
        driver.expect("find_element_by_xpath", instance)

        element = Element("name", "identifier")
        element.driver = driver

        assert element.move_mouse_over() == True
        assert element.driver.called("execute") == 1
