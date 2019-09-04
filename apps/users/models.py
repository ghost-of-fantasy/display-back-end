from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.utils import timezone


class UserProfile(AbstractUser):
    """
    用户
    """
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        ordering = ('id',)

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, unique=True, verbose_name="电话")
    add_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code