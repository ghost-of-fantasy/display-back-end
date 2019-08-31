from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from apps.user_operation.models import UserComment
from apps.user_operation.serializers import CommentSerializer
from apps.user_operation.filiters import CommentFiliter


# Create your views here.

class CommentViewSet(ListModelMixin, viewsets.GenericViewSet, CreateModelMixin):
    """评论管理API的视图"""
    queryset = UserComment.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id', 'body')  # 搜索
    ordering_fields = ('id', 'created')  # 排序
    filter_class = CommentFiliter

    def get_serializer_class(self):
        return CommentSerializer
