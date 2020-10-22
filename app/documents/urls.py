from django.urls import path, include
from .views import UserViewset, DocumentViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewset)
router.register('documents', DocumentViewset)

urlpatterns = [
    path('', include(router.urls)),
]
