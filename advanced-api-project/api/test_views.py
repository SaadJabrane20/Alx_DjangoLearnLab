from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User
from datetime import date

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Create some authors
        self.author1 = Author.objects.create(name='Victor Hugo')
        self.author2 = Author.objects.create(name='Paulo Coelho')
        
        # Create some books
        self.book1 = Book.objects.create(title='Les Miserables', publication_year=date(1989,11,4), author=self.author1)
        self.book2 = Book.objects.create(title='L\'alchemiste', publication_year=date(1994,1,1), author=self.author2)
        
        # Login URL (optional if using token auth)
        self.client.login(username='testuser', password='password123')
    def test_book_list(self):
        url = reverse('books-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    def test_book_create(self):
        url = reverse('books-create')
        data = {
            'title': 'New Book',
            'publication_year': '2025-01-01',
            'author': self.author1.id
        }
        self.client.force_login(self.user)  # Make sure user is authenticated
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')
    def test_book_create(self):
        url = reverse('books-create')
        data = {
            'title': 'New Book',
            'publication_year': '2025-01-01',
            'author': self.author1.id
        }
        self.client.force_login(self.user)  # Make sure user is authenticated
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')
    def test_book_detail(self):
        url = reverse('books-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Les Miserables')
    def test_book_update(self):
        url = reverse('books-update', args=[self.book1.id])
        data = {'title': 'Les Miserables Updated'}
        self.client.force_login(self.user)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Les Miserables Updated')
    def test_book_delete(self):
        url = reverse('books-delete', args=[self.book2.id])
        self.client.force_login(self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())
    def test_book_filtering(self):
        url = reverse('books-list') + f'?author={self.author1.id}'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Les Miserables')

    def test_book_searching(self):
        url = reverse('books-list') + '?search=alchemiste'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "L'alchemiste")

    def test_book_ordering(self):
        url = reverse('books-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.data[0]['title'], "L'alchemiste")  # newest first
