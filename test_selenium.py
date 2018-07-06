from unittest import TestCase

from selenium.webdriver.firefox.webdriver import WebDriver


class SeleniumTest(TestCase):
    """Testing google.com"""

    def test_python(self):
        self.browser = WebDriver()
        self.browser.implicitly_wait(5)
        self.browser.get('http://google.com')
        q = self.browser.find_element_by_name('q')
        q.send_keys('python')
        q.submit()
        results = self.browser.find_element_by_id('search')
        links = results.find_elements_by_tag_name('a')
        for link in links:
            if 'https://www.python.org/' in (link.get_attribute('href') or ''):
                break
        else:
            self.fail('python.com is not on google results page')
        self.browser.close()

    def test_python_in_title(self):
        self.browser = WebDriver()
        self.browser.implicitly_wait(5)
        self.browser.get('http://google.com')
        q = self.browser.find_element_by_name('q')
        q.send_keys('python')
        q.submit()
        self.browser.find_element_by_id('search')
        assert 'python' in self.browser.title
        self.browser.close()


if __name__ == '__main__':
    SeleniumTest()