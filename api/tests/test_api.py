# -*- coding: utf-8 -*-

import json
from mock import MagicMock, Mock, patch
from rest_framework.test import APIClient

from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from api.views import (
    api_overview, user_list,
    user_detail, book_list, book_publish,
    book_unpublish
)
from api.models import CustomUser


class BookTests(TestCase):
    """
    Tests for Book views
    """

    @classmethod
    def setUpClass(cls):
        super(BookTests, cls).setUpClass()
        cls.request = RequestFactory().get(reverse('api:api.books'))
        cls.view = book_list(cls.request)

    def test_get_status_code(self):
        """
        get should return a response with status code 200
        """
        response = self.client.get(reverse('api:api.books'))
        self.assertEqual(response.status_code, 200)


class CustomUserTests(TestCase):
    """
    Tests for Users
    """

    @classmethod
    def setUpClass(cls):
        super(CustomUserTests, cls).setUpClass()
        cls.request = RequestFactory().get(reverse('api:api.users'))
        cls.view = user_list(cls.request)

    def test_get_status_code(self):
        """
        get should return a response with status code 200
        """
        response = self.client.get(reverse('api:api.users'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        """
        test user post returns a status code of 201
        """
        test_data = {
            'username': 'test-user',
            'email': 'testuser@abc.com',
            'password': 'password',
            'author_pseudonym': 'mock user'
        }
        self.request.POST = test_data
        response = self.client.post(reverse('api:api.users'), data=test_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_put(self):
        """
        test user put returns a status code of 201
        """

        test_data = {
            'username': 'test-user',
            'email': 'testuser@abc.com',
            'password': 'password',
            'author_pseudonym': 'mock user'
        }
        post_response = self.client.post(reverse('api:api.users'), data=test_data, content_type='application/json')
        user_data = json.loads(post_response.content.decode('utf-8'))
        response = self.client.put(
            reverse('api:api.users.update', kwargs={'user_id': user_data['id']}),
            data=test_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_delete(self):
        """
        test user delete returns a status code of 204
        """
        test_data = {
            'username': 'test-user',
            'email': 'testuser@abc.com',
            'password': 'password',
            'author_pseudonym': 'mock user'
        }
        post_response = self.client.post(reverse('api:api.users'), data=test_data, content_type='application/json')
        user_data = json.loads(post_response.content.decode('utf-8'))
        response = self.client.delete(
            reverse('api:api.users.update', kwargs={'user_id': user_data['id']}),
        )
        self.assertEqual(response.status_code, 204)
