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
        parser.add_argument('--category_num', default=10, type=int, help='Quantity of article, category is 10')

    def handle(self, *args, **options):
        from news.fakes import fake_article, fake_category

        click.echo('Generating the category...')
        fake_category(options['category_num'])

        click.echo('Generating the article...')
        fake_article(options['article_num'])
        click.echo('Done')