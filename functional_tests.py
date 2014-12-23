#!/usr/bin/env python3
# encoding: utf-8


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        " unittest.TestCase constructor "
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        " unittest.TestCase destructor "
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User goes to access website homepage
        self.browser.get('http://localhost:8000')

        # User notices To-Do as browser page title and header
        #assert 'To-Do' in browser.title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is immediately prompted to type in a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # When user types an input and pressed enter, the item is added to the list
        inputbox.send_keys('Buy apples')

        # The item is added to the list
        # The user is immediately prompted for another item to add to the list
        inputbox.send_keys(keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Buy apples' for row in rows)
        )

        self.fail('Finish the damn test')
        # The site generates a unique URL for this list, and the user accesses this URL to verify their items were saved

        # Reminder to finish the damn unit test

if __name__ == "__main__":

    # unittest.main() launches unittest runner which
    #   finds all unittest classes/methods and runs them.
    #   warnings='ignore' Suppress some superfluous warnings (ResourceWarning)
    unittest.main(warnings='ignore')

