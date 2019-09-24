import os
import click
import django
import datetime
from django.core.management.base import BaseCommand

from display import settings
from apps.users.models import UserProfile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'display.settings')
django.setup()


class Command(BaseCommand):
    help = '用于生成管理用户的命令'

    def handle(self, *args, **options):

        start_time = datetime.datetime.now()  # 放在程序开始处

        click.echo('Generating the comment...')

        if UserProfile.objects.count() == 0:
            for user in settings.ADMINS:
                username = user[0].replace(' ', '')
                email = user[1]
                password = user[2]
                print('Creating account for %s (%s)' % (username, email))
                admin = UserProfile.objects.create_superuser(email=email, username=username, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')


        click.echo('Done')

        end_time = datetime.datetime.now()  # 放在程序结尾处
        interval = (end_time - start_time).seconds  # 以秒的形式
        final_time = interval / 60.0  # 转换成分钟
        click.echo('final_name:\t' + str(final_time))
