from rest_framework import generics, viewsets, status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import pagination
from apps.api.serializers import *

# Models
from apps.post.models import *

class PostViewSet(APIView, pagination.LimitOffsetPagination):
    """
    API endpoint 
    """

    def get(self, request, format=None):
        posts = Post.objects.filter(is_fav=True)
        results = self.paginate_queryset(posts, request, view=self)
        serializer = PostSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class PostFavViewSet(APIView):
    """
    API endpoint 
    """
    def get_object(self, pk):
        try:
            return Post.objects.get(post_id=pk)
        except Post.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet 	= self.get_object(pk)
        serializer 	= PostSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnFavAllPostViewSet(APIView):
    """
    API endpoint 
    """

    def get(self, request, format=None):
        posts = Post.objects.filter(is_fav=True).update(is_fav=False)
        return Response({
            "success":True,
            "data": [],
            "msg": "All posts unfaved"
        })













