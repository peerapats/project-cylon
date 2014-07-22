import pytest

from WebDriverMock import *
from WebElementMock import *

from project_cylon.Page import *
from project_cylon.Element import *

class TestPage:

    def test_name_return_name(self):
        page = Page("unittest", "http://www.unittest.com")
        assert page.name == "unittest"

    def test_url_return_url(self):
        page = Page("unittest", "http://www.unittest.com")
        assert page.url == "http://www.unittest.com"

    def test_get_url_return_url(self):
        page = Page("google", "http://www.google.com")
        assert page.get_url() == "http://www.google.com"

    def test_get_url_return_url_with_path(self):
        page = Page("google", "http://www.google.com")
        page.url_paths = {"login":"/login"}

        assert page.get_url("login") == "http://www.google.com/login"

    def test_find_element_return_None(self):
        page = Page("google", "http://www.google.com")
        assert page.find_element("search button") == None

    def test_find_element_return_Element(self):
        element = Element("search button", "xpath")

        page = Page("google", "http://www.google.com")
        page.elements["search button"] = element

        assert page.find_element("search button") == element

    def test_go_return_True(self):
        driver = WebDriverMock()

        page = Page("google", "http://www.google.com")
        page.driver = driver

        assert page.go() == True
        assert page.driver.called("get") == 1

    def test_wait_for_loading_return_True(self):
        driver = WebDriverMock()
        driver.expect("window_handles", [1, 2, 3])
        driver.expect("current_url", "http://www.google.com")

        page = Page("google", "http://www.google.com")
        page.driver = driver

        assert page.wait_for_loading(timeout=0) == True

    def test_wait_for_loading_return_False(self):
        driver = WebDriverMock()
        driver.expect("window_handles", [1, 2, 3])
        driver.expect("current_url", "http://www.google.co.th")

        page = Page("google", "http://www.google.com")
        page.driver = driver

        with pytest.raises(RuntimeError):
            page.wait_for_loading(timeout=0)
