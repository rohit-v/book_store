# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Book, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model. Password is not displayed on GET.
    """
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        """
        Create method for Custom User overridden to hide/hash password
        """
        try:
            user = super(CustomUserSerializer, self).create(validated_data)
            user.set_password(validated_data['password'])
            user.save()
        except Exception:
            raise serializers.ValidationError("Error creating user")
        return user

    def update(self, instance, validated_data):
        """
        Update method for Custom User overridden to hide/hash password
        """
        user = super(CustomUserSerializer, self).update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model. Password is not displayed on GET.
    """
    id = serializers.IntegerField(read_only=True)
    author = CustomUserSerializer(required=True)
    title = serializers.CharField()
    price = serializers.IntegerField()
    cover_image = serializers.URLField(max_length=500)
    description = serializers.CharField()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        """
        Create method for Book
        """
        try:
            author_data = validated_data.pop('author')
            user_objects = CustomUser.objects.filter(username=author_data.get('username'),
                                                     email=author_data.get('email'))
            if len(user_objects) == 0:
                author = CustomUser.objects.create(**author_data)
            else:
                author = user_objects.first()
            book = Book.objects.create(author=author, **validated_data)
        except Exception:
            raise serializers.ValidationError("Error creating book data")
        return book
