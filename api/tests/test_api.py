# -*- coding: utf-8 -*-

from mock import MagicMock, Mock, patch

from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from book_store.api.views import (
    api_overview, user_list,
    user_detail, book_list, book_publish,
    book_unpublish
)


class BookTests(TestCase):
    """
    Tests for Book views
    """

    @classmethod
    def setUpClass(cls):
        super(BookTests, cls).setUpClass()
        cls.request = RequestFactory().get(reverse('api:api.books'))
        cls.view = book_list()

    def test_get_status_code(self):
        """
        get should return a response of 200
        """
        response = self.client.get(reverse('api:api.books'))
        self.assertEqual(response.status_code, 200)
