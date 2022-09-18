from django.shortcuts import render
from users.models import Profile
from users.serializers import ProfileSerializers
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
        