from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist


class CreateView(generics.ListAPIView):
    """"This class defines the create behaviour of our resy api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """ save the post data when creating a new buckeltlist."""
        serializer.save()