from unittest import TestCase

from selenium.webdriver.firefox.webdriver import WebDriver


class SeleniumTest(TestCase):
    """Testing google.com"""

    def setUp(self):
        self.browser = WebDriver()
        self.browser.implicitly_wait(5)
        self.browser.get('http://google.com')

    def tearDown(self):
        self.browser.close()

    def search(self, search_string):
        q = self.browser.find_element_by_name('q')
        q.send_keys(search_string)
        q.submit()
        results = self.browser.find_element_by_id('search')
        return results.find_elements_by_tag_name('a')

    def test_python(self):

        for link in self.search('python'):
            if 'https://www.python.org/' in (link.get_attribute('href') or ''):
                break
        else:
            self.fail('python.com is not on google results page')

    def test_python_in_title(self):
        self.search('python django')
        assert 'python' in self.browser.title


if __name__ == '__main__':
    SeleniumTest()