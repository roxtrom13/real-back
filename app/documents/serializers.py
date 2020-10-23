from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Document, Category, Author


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'is_superuser', 'first_name', 'last_name', 'email']
        read_only_fields = ['id']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']


class DocumentSerializer(serializers.ModelSerializer):

    authors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Author.objects.all()
    )

    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all()
    )

    class Meta:
        model = Document
        fields = ['id', 'type', 'name', 'sumary', 'description',
                  'cover', 'document', 'is_active', 'is_premium',
                  'price', 'premium_price', 'user', 'authors', 'categories']
        read_only_fields = ['id']


class DocumentDetailSerializer(DocumentSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
