from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.news.models import Article

User = get_user_model()


# Create your models here.

class UserFav(models.Model):
    """用户收藏的文章的关系类"""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="用户")
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, verbose_name="文章")
    created = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserComment(models.Model):
    """
    评论
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                verbose_name='文章')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="用户")
    body = models.TextField(verbose_name='评论内容')
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    active = models.BooleanField(default=True, verbose_name='是否通过审核')

    class Meta:
        ordering = ('-created',)
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user.name, self.article)
