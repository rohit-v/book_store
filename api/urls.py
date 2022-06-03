# -*- coding: utf-8 -*-

from rest_framework_simplejwt import views as jwt_views

from django.urls import path, re_path

from .views import (
    api_overview, user_list,
    user_detail, book_list, book_publish,
    book_unpublish
)


app_name = 'api'

urlpatterns = [
    path('', api_overview, name='home'),
    path('books/',
         book_list,
         name='api.books'),
    path('book-publish/',
         book_publish,
         name='api.book.publish'),
    path('users/<int:user_id>/',
         user_detail),
    path('users/',
         user_list,
         name='api.users'),
    path('books/<int:book_id>/',
         book_unpublish),
    path('token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
