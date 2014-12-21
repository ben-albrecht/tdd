from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # Django's internal resolve function
        found = resolve('/')
        # Did we find a view function called home_page?
        self.assertEqual(found.func, home_page)

