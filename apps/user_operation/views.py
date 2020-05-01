from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from apps.user_operation.models import UserFav
from apps.user_operation.serializers import UserFavSerializer
from apps.utils.permissions import IsOwnerOrReadOnly


# Create your views here.


class UserFavViewSet(viewsets.GenericViewSet, CreateModelMixin, DestroyModelMixin, ListModelMixin):
    """用户收藏的功能的视图"""
    queryset = UserFav.objects.all()
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        return UserFavSerializer

    def get_queryset(self):
        """只取当前用户"""
        return UserFav.objects.filter(user=self.request.user)
