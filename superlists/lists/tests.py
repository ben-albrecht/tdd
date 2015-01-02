from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item

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

        # Django's request
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        # Compare strings instead of bytes (recall response.content is bytes)
        self.assertEqual(response.content.decode(), expected_html)

        # response.content is byte code, so we convert strings to bytes via "b'string'"
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))

    def test_home_page_can_save_a_POST_request(self):
        """
        assert that the home_page(request) returns an html file with
            To-Do lists in the title
        """

        # Django's HttpRequest object
        request = HttpRequest()
        # The request method will be POST (we are submitting data rather than GETting it)
        request.method = 'POST'
        # request.POST acts like a dictionary of attributes, and we set the 'item_text' attribute
        request.POST['item_text'] = 'a new list item'

        # We submit our request to the home_page, which communicates with the Django server(?) and returns a response
        response = home_page(request)

        # That response's content should contain the 'item_text' we provided in our POST request
        self.assertIn('a new list item', response.content.decode())

        # We replace new_item_text with our POST 'item_text', to verify our template is replacing the correct variable
        expected_html = render_to_string(
                'home.html',
                { 'new_item_text' : 'a new list item' }
                )

        # This checks that our template is working as intended
        self.assertEqual(response.content.decode(), expected_html)


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The second list item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first list item')
        self.assertEqual(second_saved_item.text, 'The second list item')


