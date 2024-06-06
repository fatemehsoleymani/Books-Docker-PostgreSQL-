from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Note Book',
            author='author1',
            price='29.00'
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Note Book')
        self.assertEqual(f'{self.book.author}', 'author1')
        self.assertEqual(f'{self.book.price}', '29.00')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Note Book')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('books/123/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'author1')
        self.assertTemplateUsed(response, 'books/book_detail.html')