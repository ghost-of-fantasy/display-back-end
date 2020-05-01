from django.db import models

# Create your models here.
class UserOperation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    remote_addr = models.CharField(max_length=64, blank=True, null=True)
    time_local = models.DateTimeField(blank=True, null=True)
    http_method = models.CharField(max_length=32, blank=True, null=True)
    http_url = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    body_bytes_sent = models.BigIntegerField(blank=True, null=True)
    http_referer = models.CharField(max_length=128, blank=True, null=True)
    http_user_agent = models.CharField(max_length=256, blank=True, null=True)
    res_type = models.CharField(max_length=64, blank=True, null=True)
    res_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        verbose_name = '用户行为'
        verbose_name_plural = verbose_name
        db_table = 'monitor_user_operation'


class VisitorCount(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    vis_type = models.CharField(max_length=32, blank=True, null=True)
    res_type = models.CharField(max_length=64, blank=True, null=True)
    res_id = models.CharField(max_length=64, blank=True, null=True)
    time_type = models.CharField(max_length=32, blank=True, null=True)
    time_local = models.DateTimeField(blank=True, null=True)
    click = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        verbose_name = '访问量'
        verbose_name_plural = verbose_name
        db_table = 'monitor_visitor_count'