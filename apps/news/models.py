from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class Article(models.Model):
    """文章"""
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    id = models.AutoField(primary_key=True, verbose_name='ID')
    website_name = models.CharField(max_length=50, verbose_name='来源网站的名称')
    url = models.CharField(max_length=500, unique=True, verbose_name='文章链接')
    title = models.CharField(max_length=250, verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')
    publish_time = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published', verbose_name='状态')
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish_time',)
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


