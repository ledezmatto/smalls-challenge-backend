from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# Models
from apps.post.models import *


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude= ('id',)