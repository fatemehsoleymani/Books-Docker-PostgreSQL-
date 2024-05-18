from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomePageTest(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_home_page_html_contain(self):
        self.assertContains(self.response, 'Home Page')

    def test_home_page_does_not_correct_html(self):
        self.assertNotContains(self.response, 'hi from here')

    def test_home_page_resolves_home_page_view(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__, HomePageView.as_view().__name__
        )
