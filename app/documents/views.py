from rest_framework import generics, viewsets
from .models import Document
from .serializers import DocumentSerializer, UserSerializer
from django.contrib.auth import get_user_model


class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
