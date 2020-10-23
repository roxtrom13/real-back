from rest_framework import viewsets
from .models import Document, Author, Category
from documents import serializers
from django.contrib.auth import get_user_model


class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = serializers.DocumentSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.DocumentDetailSerializer
        return self.serializer_class


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
