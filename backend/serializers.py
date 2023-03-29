from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['user_permissions', 'is_active', 'is_staff', 'last_name', 'first_name', 
                'last_login', 'date_joined']
        def create(self, validated_data):
            user = User(
                email=validated_data['email'],
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class postSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = post
        fields = '__all__'

class postReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = postReview
        fields = '__all__'

class subscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscribedUsers
        fields = '__all__'

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'
