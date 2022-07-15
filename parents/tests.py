from django.test import TestCase
from django.urls import resolve
from parents.views import home_page


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(response.status_code, 200)

    # def test_table_adds_