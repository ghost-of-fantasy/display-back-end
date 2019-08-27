import random
import pytz
from faker import Faker
from apps.news.models import Article, Comment

fake = Faker("zh_CN")


def fake_article(count=50):
    """生成假文章"""

    for i in range(count):
        try:
            article = Article(
                website_name=fake.name(),  # 来源网站的名称
                url=fake.uri(),  # 文章链接
                title=fake.sentence(),  # 文章标题
                content=fake.text(2000),  # 文章内容
                publish_time=fake.date_time_this_year(tzinfo=pytz.UTC)
            )
            article.save()
            for i in range(random.randint(1, 4)):
                article.tags.add(fake.word())

        except Exception as e:
            print(e)


def fake_comment(count=500):
    """生成假评论数据的函数"""
    articles = Article.objects.values_list('id')
    articles_count = Article.objects.count()

    for i in range(count):
        article = articles[random.randint(0, articles_count - 1)][0]
        try:
            Comment.objects.get_or_create(
                article=Article.objects.get(id=article),
                name=fake.name(),  # 来源网站的名称
                email=fake.email(),  # 文章链接
                body=fake.text(100),  # 文章标题
                created=fake.date_time_this_year(tzinfo=pytz.UTC)
            )
        except Exception as e:
            print(e)
