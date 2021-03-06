import os
import click
import django
import datetime
from django.core.management.base import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'display.settings')
django.setup()


class Command(BaseCommand):
    help = '用于生成用户操作的假数据的命令'

    def add_arguments(self, parser):
        parser.add_argument('--comment_num', default=500, type=int, help='Quantity of comment, default is 500')

    def handle(self, *args, **options):
        from user_operation.fakes import fake_comment

        start_time = datetime.datetime.now()  # 放在程序开始处

        click.echo('Generating the comment...')
        fake_comment(options['comment_num'])

        click.echo('Done')

        end_time = datetime.datetime.now()  # 放在程序结尾处
        interval = (end_time - start_time).seconds  # 以秒的形式
        final_time = interval / 60.0  # 转换成分钟
        click.echo('final_name:\t' + str(final_time))
