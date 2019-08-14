from django.db import models
from django.utils import timezone


# Create your models here.

class Article(models.Model):
    website_name = models.CharField(max_length=50)  # 来源网站的名称
    url = models.CharField(max_length=500, primary_key=True)  # 文章链接
    title = models.CharField(max_length=250)  # 文章内容
    content = models.TextField()  # 文章内容
    category = models.CharField(max_length=50)  # 文章类型
    publish_time = models.DateTimeField(default=timezone.now)  # 发布时间
    created = models.DateTimeField(auto_now_add=True)  # 创建时间
    updated = models.DateTimeField(auto_now=True)  # 更新时间

    class Meta:
        ordering = ('-publish_time',)

    def __str__(self):
        return self.title
