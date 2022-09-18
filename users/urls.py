from django.urls import path,include
from users.views import UserViewSet, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [

    path('',include(router.urls)),
    
]
