from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=128)
    img_path = models.CharField(max_length=256, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor_game'
        verbose_name = '游戏'
        verbose_name_plural = verbose_name

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
    click = models.BigIntegerField(default=0, verbose_name='点击次数')
    creator = models.CharField(default='niracler', max_length=64, verbose_name='创建者用户名')
    publish_time = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='状态')
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish_time',)
        verbose_name = '游戏新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Event(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128,unique=True, verbose_name='事件名称')
    articles = models.ManyToManyField(Article, related_name='articles', verbose_name='新闻列表')
    creator = models.CharField(default='niracler', max_length=64, verbose_name='创建者用户名')
    click = models.BigIntegerField(default=0, verbose_name='点击次数')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(default=timezone.now, verbose_name='更新时间')

    class Meta:
        ordering = ('-updated',)
        verbose_name = '游戏新闻事件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
