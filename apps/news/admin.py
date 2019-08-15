from django.contrib import admin
from .models import Article, Category


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_time', 'status')
    list_filter = ('publish_time', 'status')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish_time'
    ordering = ('status', 'publish_time')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')
    list_filter = ('created',)
    search_fields = ('name',)
    date_hierarchy = 'created'
    ordering = ('created', )
