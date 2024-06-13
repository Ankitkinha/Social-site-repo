from rest_framework import serializers

from .models import User, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'mobile_no', 'email', 'created_on', 'updated_on', 'is_staff',
                  'is_active', 'is_superuser']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'image', 'created_on', 'updated_on', 'view_count']

