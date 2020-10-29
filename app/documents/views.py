from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import (Document, Author, Category, Download, DocumentDetail,
                     Subscription, Payment, UserSubscription)
from documents import serializers
from django.contrib.auth import get_user_model


class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)


class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = serializers.DocumentSerializer

    def _params_to_ints(self, qs):
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        categories = self.request.query_params.get('categories')
        authors = self.request.query_params.get('authors')
        queryset = self.queryset
        if categories:
            category_ids = self._params_to_ints(categories)
            queryset = queryset.filter(categories__id__in=category_ids)
        if authors:
            author_ids = self._params_to_ints(authors)
            queryset = queryset.filter(authors__id__in=author_ids)

        return queryset

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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.DownloadDetailSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.UserSubscriptionDetailSerializer
        return self.serializer_class
