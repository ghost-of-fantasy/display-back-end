"""display URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from news.views import UserViewSet, GroupViewSet, ArticleViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)  # 用户管理api
router.register(r'groups', GroupViewSet)  # 用户组管理api
router.register(r'article', ArticleViewSet)  # 文章管理api
router.register(r'category', CategoryViewSet)  # 文章类别管理api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls', namespace='news')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]
