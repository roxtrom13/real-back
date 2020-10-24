from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (Document, Category, Author, Download, DocumentDetail,
                     Subscription, Payment, UserSubscription)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'is_superuser']
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


class DownloadSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )

    document = serializers.PrimaryKeyRelatedField(
        queryset=Document.objects.all()
    )

    class Meta:
        model = Download
        fields = ['id', 'downloads_number', 'user', 'document']
        read_only_fields = ['id']


class DownloadDetailSerializer(DownloadSerializer):
    user = UserSerializer(read_only=True)
    document = DocumentSerializer(read_only=True)


class DocumentDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentDetail
        fields = ['id', 'name', 'value', 'document']
        read_only_fields = ['id']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'name', 'description', 'price', 'is_active']
        read_only_fields = ['id']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'paypal_id', 'status', 'amount']
        read_only_fields = ['id']


class UserSubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )
    payment = serializers.PrimaryKeyRelatedField(
        queryset=Payment.objects.all()
    )
    subscription = serializers.PrimaryKeyRelatedField(
        queryset=Subscription.objects.all()
    )

    class Meta:
        model = UserSubscription
        fields = ['id', 'user', 'subscription',
                  'payment', 'start_date', 'end_date']
        read_only_fields = ['id']


class UserSubscriptionDetailSerializer(UserSubscriptionSerializer):
    user = UserSerializer(read_only=True)
    payment = PaymentSerializer(read_only=True)
    subscription = SubscriptionSerializer(read_only=True)
