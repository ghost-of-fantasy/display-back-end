from django.contrib import admin
from .models import  UserProfile

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """用户信息管理类"""
    list_display = ('id', 'username', 'email', 'mobile')