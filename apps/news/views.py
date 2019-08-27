from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from apps.news.serializers import UserSerializer, GroupSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from apps.news.filiters import ArticleFiliter, CommentFiliter
from apps.news.models import Article, Comment
from apps.news.serializers import ArticleSerializer, CommentSerializer, TagSerializer, \
    ArticleCreateSerializer
from taggit.models import Tag


# Create your views here.

class ArticlePagination(PageNumberPagination):
    """用于文章内容API分页的类"""
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class TagsPagination(PageNumberPagination):
    """用于文章内容API分页的类"""
    page_size = 30
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class ArticleViewSet(ListModelMixin, viewsets.GenericViewSet, CreateModelMixin):
    """文章管理API的视图"""
    queryset = Article.objects.all()
    pagination_class = ArticlePagination  # 分页函数
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ArticleFiliter
    search_fields = ('id', 'content')  # 搜索
    ordering_fields = ('id', 'publish_time')  # 排序

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        elif self.action == 'create':
            return ArticleCreateSerializer


class TagViewSet(ListModelMixin, viewsets.GenericViewSet, CreateModelMixin):
    """文章类型管理API的视图"""
    tag_queryset = Tag.objects.all()
    queryset = tag_queryset.annotate(num_times=Count('taggit_taggeditem_items'))
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    pagination_class = TagsPagination
    ordering_fields = ('id', 'num_times')

    def get_serializer_class(self):
        return TagSerializer


class CommentViewSet(ListModelMixin, viewsets.GenericViewSet, CreateModelMixin):
    """评论管理API的视图"""
    queryset = Comment.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id', 'body')  # 搜索
    ordering_fields = ('id', 'created')  # 排序
    filter_class = CommentFiliter

    def get_serializer_class(self):
        return CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
