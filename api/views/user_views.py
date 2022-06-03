# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from api.models import CustomUser, Book
from api.serializers import CustomUserSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, user_id):
    """
    Retrieve, update or delete a user.
    """
    try:
        user = CustomUser.objects.get(pk=user_id)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def book_unpublish(request, book_id):
    """
    Un publish a book
    """
    if request.user:
        user_id = request.user.id
    else:
        user_id = None
    try:
        book = Book.objects.filter(pk=book_id, author__id=user_id).first()
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if book and book.author and book.author.author_pseudonym not in ['', 'Anonymous']:
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'detail': "Verify author details"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_404_NOT_FOUND)
