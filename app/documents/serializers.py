from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Document, Category, Author


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
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
        fields = ['id', 'type', 'name', 'sumary', 'description', 'cover', 'document', 'is_active',
                  'is_premium', 'price', 'premium_price', 'user', 'authors', 'categories']
        read_only_fields = ['id']
