from django.urls import path, include
from documents import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewset)
router.register('documents', views.DocumentViewset)
router.register('authors', views.AuthorViewset)
router.register('categories', views.CategoryViewset)

urlpatterns = [
    path('', include(router.urls)),
]
