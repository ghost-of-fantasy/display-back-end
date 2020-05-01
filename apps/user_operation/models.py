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
    created = models.DateTimeField(default=timezone.now, verbose_name="添加时间")

    class Meta:
        ordering = ('-created',)
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name
        unique_together = ("user", "article")

    def __str__(self):
        return self.user.name