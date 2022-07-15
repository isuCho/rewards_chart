import unittest
from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_open_home_page(self):
        # Catherine hears about an online kids rewards app.
        # She goes to check out the homepage
        self.browser.get('http://localhost:8000')
        sleep(3)
        self.fail('Finish the test!')

        # She is invited to add a child's name.
        # She enters 'Yuna' into the textbox provided
        # When she hits 'enter', the page refreshes and now the page shows 'Yuna', and 'add another child'

        # There is a textbox underneath 'Yuna' that lets her add a task, as well as points.

        # She types 'clean bedroom' into the textbox, and 50 points.
        # When she hits 'enter' the page refreshes and there is an entry underneath 'Yuna'
        # listing 'clean bedroom' and 50 points.

        # There is another textbox underneath 'Yuna'.
        # She enters 'practice clarinet' and 30 points. The page updates again, and shows both of Yuna's tasks
        # underneath her name.


if __name__ == '__main__':
    unittest.main()
