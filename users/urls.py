from django.urls import path,include
from users.views import UserViewSet, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [

    path('',include(router.urls)),
    
]
