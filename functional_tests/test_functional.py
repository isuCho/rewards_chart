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

        # She notices the title mention a rewards chart
        self.assertIn('Rewards chart', self.browser.title)

        # She is invited to enter a child's name.
        inputbox = self.browser.find_element(By.ID, 'id_new_child')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            "What's your child's name?"
        )

        # She enters 'Yuna' into the textbox provided
        inputbox.send_keys('Yuna')
        # When she hits 'enter', the page refreshes and now the page shows 'Yuna'
        inputbox.send_keys(Keys.ENTER)
        sleep(2)

        children = self.browser.find_element(By.ID, 'id_children_table')
        rows = children.find_elements(By.TAG_NAME, 'h2')
        self.assertIn('Yuna', [row.text for row in rows])

        # There is a textbox underneath 'Yuna' that lets her add a task, points for the task, and submit
        taskbox = self.browser.find_element(By.ID, 'id_new_task')
        self.assertEqual(
            taskbox.get_attribute('placeholder'),
            'Enter a task'
        )
        pointbox = self.browser.find_element(By.ID, 'id_point')
        self.assertEqual(
            pointbox.get_attribute('placeholder'),
            'And the points'
        )
        submitbutton = self.browser.find_element(By.NAME, 'submit')

        # She types 'clean bedroom' into the textbox, and 50 points.
        taskbox.send_keys('Clean bedroom')
        pointbox.send_keys('50')
        # When she presses 'submit' the page refreshes and there is an entry underneath 'Yuna'
        submitbutton.click()
        # listing 'clean bedroom' and 50 points.
        tasktable = self.browser.find_element(By.ID, 'id_task_table')
        cells = tasktable.find_elements(By.TAG_NAME, 'td')
        self.assertIn('Clean bedroom', [cell.text for cell in cells])
        self.assertIn('50', [cell.text for cell in cells])

        self.fail('Finish the test!')
        # There is another textbox underneath 'Yuna'.
        # She enters 'practice clarinet' and 30 points. The page updates again, and shows both of Yuna's tasks
        # underneath her name.
