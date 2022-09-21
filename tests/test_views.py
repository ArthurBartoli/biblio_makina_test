from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_main_page_displaying_correctly(self):
        """The main page displays correctly"""
        response = self.client.get('http://0.0.0.0:8000')
        self.assertEqual(response.status_code, 200)


