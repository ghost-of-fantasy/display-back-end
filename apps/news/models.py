from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    """文章类型"""
    id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=50, null=False, unique=True, verbose_name='类型名称')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-created',)
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


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
    category = models.ForeignKey(Category, models.DO_NOTHING, verbose_name='文章类型')
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


class Comment(models.Model):
    """评论"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comment', verbose_name='文章')
    name = models.CharField(max_length=80, verbose_name='评论人名称')
    email = models.EmailField(verbose_name='评论人邮件地址')
    body = models.TextField(verbose_name='评论内容')
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    active = models.BooleanField(default=True, verbose_name='是否通过审核')

    class Meta:
        ordering = ('-created',)
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.article)
