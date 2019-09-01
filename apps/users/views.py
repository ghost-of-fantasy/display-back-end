from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from apps.users.models import UserProfile
from apps.users.serializers import UserSerializer


# Create your views here.

class UserViewSet(ListModelMixin, viewsets.GenericViewSet, CreateModelMixin):
    """评论管理API的视图"""
    queryset = UserProfile.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id', 'body')  # 搜索
    ordering_fields = ('id', 'created')  # 排序

    def get_serializer_class(self):
        return UserSerializer
