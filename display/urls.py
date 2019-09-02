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
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from news.views import ArticleViewSet, TagViewSet
from user_operation.views import CommentViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)  # 文章管理api
router.register(r'comment', CommentViewSet)  # 评论管理api
router.register(r'tag', TagViewSet)  # 评论管理api
router.register(r'user', UserViewSet)  # 用户管理api

# 后面执行的会覆盖前面执行的
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # # drf自带的token认证机制
    # path('api-token-auth/', views.obtain_auth_token),

    path('login/', obtain_jwt_token),

    path('api/', include(router.urls)),
]
