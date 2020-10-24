from django.urls import path, include
from documents import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewset)
router.register('documents', views.DocumentViewset)
router.register('authors', views.AuthorViewset)
router.register('categories', views.CategoryViewset)
router.register('downloads', views.DownloadViewset)
router.register('detailed-documents', views.DocumentDetailViewset)
router.register('subscriptions', views.SubscriptionViewset)
router.register('payments', views.PaymentViewset)
router.register('user-subscriptions', views.UserSubscriptionViewset)

urlpatterns = [
    path('', include(router.urls)),
]
