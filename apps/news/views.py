from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from apps.news.serializers import UserSerializer, GroupSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from apps.news.filiters import ArticleFiliter
from apps.news.models import Article, Category
from apps.news.serializers import ArticleSerializer, CategorySerializer


# Create your views here.

class ArticlePagination(PageNumberPagination):
    """用于文章内容分页的视图"""
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class ArticleViewSet(ListModelMixin, viewsets.GenericViewSet, CreateModelMixin):
    """文章管理的视图"""
    queryset = Article.objects.all()
    pagination_class = ArticlePagination  # 分页函数
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ArticleFiliter
    search_fields = ('id', 'content')  # 搜索
    ordering_fields = ('id', 'publish_time')  # 排序

    def get_serializer_class(self):
        return ArticleSerializer


class CategoryViewSet(ListModelMixin, viewsets.GenericViewSet, CreateModelMixin):
    """文章类型管理的视图"""
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id', 'name')  # 搜索
    ordering_fields = ('id', 'created')  # 排序
    pagination_class = None

    def get_serializer_class(self):
        return CategorySerializer


# Create your views here.

def article_list(request):
    """
    文章列表视图
    :param request:
    :return:
    """
    articles = Article.objects.get_queryset().filter(status='published')
    return render(request, 'news/article/list.html', {'articles': articles})


def article_detail(request, id):
    """
    文章详细内容视图
    :param request:
    :param id:
    :return:
    """
    article = get_object_or_404(Article, id=id)
    return render(request, 'news/article/detail.html', {'article': article})


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
