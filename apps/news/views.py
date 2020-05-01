from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from apps.news.filiters import ArticleFiliter
from apps.news.models import Article
from apps.news.serializers import ArticleSerializer, TagSerializer, \
    ArticleCreateSerializer
from taggit.models import Tag
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_extensions.cache.mixins import CacheResponseMixin


# Create your views here.

class Pagination(PageNumberPagination):
    """用于文章内容API分页的类"""
    page_size = 10
    page_size_query_param = 'ps'
    page_query_param = 'p'
    max_page_size = 100


class ArticleViewSet(CacheResponseMixin, ListModelMixin, viewsets.GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    """文章管理API的视图"""
    queryset = Article.objects.all()
    pagination_class = Pagination  # 分页函数
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ArticleFiliter
    search_fields = ('id', 'content')  # 搜索
    ordering_fields = ('id', 'publish_time', 'created')  # 排序

    def get_serializer_class(self):
        if self.action == 'create':
            return ArticleCreateSerializer
        else :
            return ArticleSerializer


class TagViewSet(CacheResponseMixin, ListModelMixin, viewsets.GenericViewSet):
    """文章类型管理API的视图"""
    tag_queryset = Tag.objects.all()
    queryset = tag_queryset.annotate(num_times=Count('taggit_taggeditem_items'))
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    pagination_class = Pagination
    ordering_fields = ('id', 'num_times')
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_serializer_class(self):
        return TagSerializer
