from django.urls import path
from .views import UserList, UserDetail, DocumentList, DocumentDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('', DocumentList.as_view()),
    path('<int:pk>/', DocumentDetail.as_view())
]
