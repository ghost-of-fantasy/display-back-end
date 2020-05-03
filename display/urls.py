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
from django.views.static import serve
from display.settings import MEDIA_ROOT, STATIC_ROOT
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from news.views import ArticleViewSet, TagViewSet, EventViewSet
from user_operation.views import UserFavViewSet
from users.views import UserViewSet, SmsCodeViewSet
from django.urls import path
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet, base_name='article')  # 文章管理api
router.register(r'tag', TagViewSet, base_name='tag')  # 新闻标签管理api
router.register(r'event', EventViewSet, base_name='event')  # 新闻事件管理api
router.register(r'register', UserViewSet, base_name='register')  # 用户管理api
router.register(r'code', SmsCodeViewSet, base_name="code")  # 验证码api
router.register(r'userfav', UserFavViewSet, base_name="userfav")  # 用户收藏api

# 后面执行的会覆盖前面执行的
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # # drf自带的token认证机制
    # path('api-token-auth/', views.obtain_auth_token),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    path('login/', obtain_jwt_token),
    path('api/', include(router.urls)),
]
