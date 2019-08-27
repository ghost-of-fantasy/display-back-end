from django.contrib import admin
from .models import Article, Comment


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """文章管理类"""
    list_display = ('id', 'title', 'publish_time', 'status')
    list_filter = ('publish_time', 'status')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish_time'
    ordering = ('status', 'publish_time')



@admin.register(Comment)
class CommitAdmin(admin.ModelAdmin):
    """评论管理类"""
    list_display = ('id', 'name', 'email' , 'article', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name',)
    date_hierarchy = 'created'
    ordering = ('created',)
