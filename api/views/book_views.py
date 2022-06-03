# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from api.models import Book
from api.serializers import BookSerializer


@api_view(['GET'])
def api_overview(request):
    # Creating a swagger doc with all the request parameters and headers would be a better way
    # Accept Header defines the response type
    api_urls = {
        'Get all Users or Create a user': 'GET/POST api/users/',
        'Update or Delete a user': 'PUT/DELETE /api/users/<user_id>/',
        'Get a book (filter params: title, author_id, price)': 'GET /api/books?subcategory=value',
        'Un publish a book (needs Authorization: Bearer <token>)': 'DELETE /api/books/<book_id>',
        'Get JWT token': 'POST /api/token'
    }

    return JsonResponse(api_urls)


@api_view(['GET'])
def book_list(request):
    """
    List all books.
    Query parameters currently supported: title, author_id and price
    """
    books = Book.objects.all()
    if request.GET.get('title'):
        books = books.filter(title=request.GET.get('title'))
    if request.GET.get('author_id'):
        books = books.filter(author__id=request.GET.get('author_id'))
    if request.GET.get('price'):
        books = books.filter(price=int(request.GET.get('price')))
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def book_publish(request):
    """
    Create book and author
    Headers:
        - Authorization : Bearer <token>
        - Accept : application/xml or application/json
    REQUEST BODY expected:
    {
        "title": "",
        "description": "",
        "price": 20,
        ...
    }

    returns: Created book object
    """
    if request.user:
        request.data['author'] = model_to_dict(request.user)
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

