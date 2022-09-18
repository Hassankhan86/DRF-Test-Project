from django.shortcuts import render
from users.models import Post, Profile
from users.serializers import ProfileSerializers, PostSerializers
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from users.permissions import ReviewUserorReadOnly
from rest_framework import status

    
class UserViewSet(viewsets.ViewSet):
    permission_classes = [ReviewUserorReadOnly]
    def list(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Profile.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProfileSerializers(user)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = Profile.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProfileSerializers(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class PostViewSet(viewsets.ViewSet):
    # permission_classes = [ReviewUserorReadOnly]
    # permission_classes = [IsAuthenticated]
    def list(self, request):
        try:
            queryset =  Post.objects.filter(owner__email = request.user.email)
            serializer = PostSerializers(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response('AnonymousUser Please Login First',status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        try:
            queryset = Post.objects.filter(owner__email = request.user.email)
            user = get_object_or_404(queryset, pk=pk)
            serializer = PostSerializers(user)
            return Response(serializer.data)
        except:
            return Response('AnonymousUser Please Login First',status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            post_data = request.data
            post = Post.objects.create(title = post_data['title'], content = post_data['content'], owner = request.user,  )
            serializer = PostSerializers(post)
            return Response(serializer.data)
        except:
            return Response('AnonymousUser Please Login First',status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            queryset = Post.objects.all()
            user = get_object_or_404(queryset, pk=pk)
            serializer = PostSerializers(user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response('AnonymousUser Please Login First',status=status.HTTP_400_BAD_REQUEST)
