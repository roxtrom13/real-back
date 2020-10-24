from rest_framework import viewsets
from .models import (Document, Author, Category, Download, DocumentDetail,
                     Subscription, Payment, UserSubscription)
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


class DownloadViewset(viewsets.ModelViewSet):
    queryset = Download.objects.all()
    serializer_class = serializers.DownloadSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.DownloadDetailSerializer
        return self.serializer_class


class DocumentDetailViewset(viewsets.ModelViewSet):
    queryset = DocumentDetail.objects.all()
    serializer_class = serializers.DocumentDetailedSerializer


class SubscriptionViewset(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = serializers.SubscriptionSerializer


class PaymentViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


class UserSubscriptionViewset(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = serializers.UserSubscriptionSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.UserSubscriptionDetailSerializer
        return self.serializer_class
