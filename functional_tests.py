#!/usr/bin/env python3
# encoding: utf-8


from selenium import webdriver
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

        # User notices To-Do as browser page title
        #assert 'To-Do' in browser.title
        self.assertIn('To-Do', self.browser.title)

        # Reminder to finish the damn unit test
        self.fail('Finish the damn test')

        # User is immediately prompted to type in a to-do item

        # When user types an input and pressed enter, the item is added to the list

        # The user is immediately prompted for another item to add to the list

        # The site generates a unique URL for this list, and the user accesses this URL to verify their items were saved


if __name__ == "__main__":

    # unittest.main() launches unittest runner which
    #   finds all unittest classes/methods and runs them.
    #   warnings='ignore' Suppress some superfluous warnings (ResourceWarning)
    unittest.main(warnings='ignore')

