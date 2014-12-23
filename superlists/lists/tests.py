from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Unit Tests

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """
        Assert that the root url resolves to the homepage
        """

        # Django's internal resolve function
        found = resolve('/')

        # Did we find a view function called home_page?
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        """
        assert that the home_page(request) returns an html file with
            To-Do lists in the title
        """

        # Django's
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        # Compare strings instead of bytes (recall response.content is bytes)
        self.assertEqual(response.content.decode(), expected_html)

        # response.content is byte code, so we convert strings to bytes via "b'string'"
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
