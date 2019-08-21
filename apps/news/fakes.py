import random
import pytz
from faker import Faker
from apps.news.models import Article, Category, Comment

fake = Faker("zh_CN")


def fake_category(count=10):
    """生成假的文章类型"""
    for i in range(count):
        Category.objects.get_or_create(
            name=fake.word()
        )


def fake_article(count=50):
    """生成假文章类型"""
    categorys = Category.objects.values_list('name')
    category_count = Category.objects.count()

    for i in range(count):
        category = categorys[random.randint(0, category_count - 1)][0]
        try:
            Article.objects.get_or_create(
                website_name=fake.name(),  # 来源网站的名称
                url=fake.uri(),  # 文章链接
                title=fake.sentence(),  # 文章标题
                content=fake.text(2000),  # 文章内容
                category=Category.objects.get(name=category),  # 文章类型
                publish_time=fake.date_time_this_year(tzinfo=pytz.UTC)
            )
        except Exception as e:
            print(e)


def fake_comment(count=500):
    """生成假评论数据的函数"""
    articles = Article.objects.values_list('id')
    articles_count = Category.objects.count()

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
