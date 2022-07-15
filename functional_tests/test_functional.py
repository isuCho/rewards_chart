import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_child_and_tasks(self):
        # Catherine hears about an online kids rewards app.
        # She goes to check out the homepage
        self.browser.get('http://localhost:8000')

        # She notices the title and header mention a rewards chart
        self.assertIn('Rewards chart', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Rewards chart', header_text)

        # She is invited to enter a child's name.
        inputbox = self.browser.find_element(By.ID, 'id_new_child')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            "Enter your child's name"
        )

        # She enters 'Yuna' into the textbox provided
        inputbox.send_keys('Yuna')
        # When she hits 'enter', the page refreshes and now the page shows 'Yuna'
        inputbox.send_keys(Keys.ENTER)
        sleep(2)

        table = self.browser.find_element(By.ID, 'id_children_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == 'Yuna' for row in rows)
        )

        # There is a textbox underneath 'Yuna' that lets her add a task, as well as points.
        self.fail('Finish the test!')

        # She types 'clean bedroom' into the textbox, and 50 points.
        # When she hits 'enter' the page refreshes and there is an entry underneath 'Yuna'
        # listing 'clean bedroom' and 50 points.

        # There is another textbox underneath 'Yuna'.
        # She enters 'practice clarinet' and 30 points. The page updates again, and shows both of Yuna's tasks
        # underneath her name.
