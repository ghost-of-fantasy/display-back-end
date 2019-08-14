# from django.test import TestCase
from faker import Faker
from news.models import Article

# Create your tests here.

fake = Faker()


def fake_article(count=50):
    for i in range(count):
        article = Article(
            website_name=fake.name(),  # 来源网站的名称
            url=fake.url(),  # 文章链接
            title=fake.sentence(),  # 文章标题
            content=fake.text(2000),  # 文章内容
            category=fake.sentence(),  # 文章类型
            publish_time=fake.date_time_this_year()  # 发布时间
        )
        article.save()