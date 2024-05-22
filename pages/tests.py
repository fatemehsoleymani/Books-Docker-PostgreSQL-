from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView


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


class AboutPageTest(TestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_status_code(self):
        self.assertTrue(self.response.status_code, 200)
        self.assertContains(self.response, 'About Page')
        self.assertNotContains(self.response, 'Hello from about page')
        self.assertTemplateUsed(self.response, 'about.html')

    def test_about_page_url_resolves_about_page_view(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__, AboutPageView.as_view().__name__
        )