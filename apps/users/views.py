from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from apps.users.models import UserProfile
from apps.users.serializers import UserSerializer

User = get_user_model()  # 这样导入的话，到时候就可以方便地更新用户类了


# Create your views here.

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewSet(ListModelMixin, viewsets.GenericViewSet, CreateModelMixin):
    """评论管理API的视图"""
    queryset = UserProfile.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id', 'body')  # 搜索
    ordering_fields = ('id', 'created')  # 排序

    def get_serializer_class(self):
        return UserSerializer
