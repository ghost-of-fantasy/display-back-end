from django.contrib import admin
from .models import Article, Game, Event


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """文章管理类"""
    list_display = ('id', 'title','creator', 'click', 'publish_time', 'status')
    list_filter = ('publish_time', 'status')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish_time'
    ordering = ('status', 'publish_time')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """游戏管理类"""
    list_display = ('id', 'name',  'img_path', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('name', )
    date_hierarchy = 'created_at'
    ordering = ('created_at', )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """游戏新闻事件管理类"""
    list_display = ('id', 'name', 'creator', 'click', 'created', 'updated')
    list_filter = ('creator',)
    search_fields = ('name', 'description')
    date_hierarchy = 'created'
    ordering = ('created', 'name')
