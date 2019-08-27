import os
import click
import django
from django.core.management.base import BaseCommand

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'display.settings')
django.setup()


class Command(BaseCommand):
    help = '用于生成假数据的命令'

    def add_arguments(self, parser):
        parser.add_argument('--article_num', default=50, type=int, help='Quantity of article, default is 50')
        parser.add_argument('--comment_num', default=500, type=int, help='Quantity of comment, default is 500')

    def handle(self, *args, **options):
        from news.fakes import fake_article,  fake_comment

        click.echo('Generating the article...')
        fake_article(options['article_num'])

        click.echo('Generating the comment...')
        fake_comment(options['comment_num'])
        click.echo('Done')
