# # -*- coding: utf-8 -*-
#
# from mock import MagicMock, Mock, patch
#
# from django.test import TestCase
# from django.test.client import RequestFactory
# from django.urls import reverse
#
# from book_store.api.views import (
#     api_overview, user_list,
#     user_detail, book_list, book_publish,
#     book_unpublish
# )
#
#
# class BookTests(TestCase):
#     """
#     Tests for Book views
#     """
#
#     @classmethod
#     def setUpClass(cls):
#         super(BookTests, cls).setUpClass()
#         cls.request = RequestFactory().get(reverse('api:api.books'))
#         cls.view = book_list()
#
#     def test_get_status_code(self):
#         """
#         get should return a response of 200
#         """
#         response = self.client.get(reverse('api:api.books'))
#         self.assertEqual(response.status_code, 200)
#
#
#     # @patch('genome.views.UploadFileView.get_form')
#     # @patch('genome.views.handle_uploaded_file')
#     # @patch('genome.views.messages')
#     # def test_post_form_valid_redirect(self, mock_messages, mock_file_upload, mock_get_form):
#     #     """
#     #     post should return a status code of 302 on success.
#     #     """
#     #     mock_get_form.return_value.is_valid.return_value = True
#     #     request = Mock()
#     #     request.FILES = {'genome_file': MagicMock()}
#     #     response = self.view.post(request)
#     #     self.assertEqual(response.status_code, 302)
#     #
#     # @patch('genome.views.UploadFileView.get_form')
#     # @patch('genome.views.handle_uploaded_file')
#     # @patch('genome.views.messages')
#     # def test_post_form_valid_success_message(self, mock_messages, mock_file_upload, mock_get_form):
#     #     """
#     #     post should create a success message when form is valid.
#     #     """
#     #     mock_get_form.return_value.is_valid.return_value = True
#     #     request = Mock()
#     #     request.FILES = {'genome_file': MagicMock()}
#     #     self.view.post(request)
#     #     mock_messages.success.assert_called_once_with(request, "Successfully uploaded.")
#
#     # @patch('genome.views.UploadFileView.get_form')
#     # @patch('genome.views.handle_uploaded_file')
#     # @patch('genome.views.messages')
#     # def test_post_form_valid_upload_handler(self, mock_messages, mock_file_upload, mock_get_form):
#     #     """
#     #     post should call handle_uploaded_file when the form is valid.
#     #     """
#     #     mock_get_form.return_value.is_valid.return_value = True
#     #     request = Mock()
#     #     request.FILES = {'genome_file': MagicMock()}
#     #     self.view.post(request)
#     #     mock_file_upload.assert_called_once_with(request.FILES['genome_file'])
#
#
# # class DisplayViewTests(TestCase):
# #     """
# #     Tests for display view
# #     """
# #
# #     def test_get_status_code(self):
# #         """
# #         get should return a response of 200
# #         """
# #         response = self.client.get(reverse('genome:display'))
# #         self.assertEqual(response.status_code, 200)
# #
# #     def test_get_template_name(self):
# #         """
# #         get should return a response with
# #         template set to display.html
# #         """
# #         response = self.client.get(reverse('genome:display'))
# #         response_template_names = [template.name for template in response.templates]
# #         self.assertIn('genome/display.html', response_template_names)
