import random
import pytz
from faker import Faker
from apps.news.models import Article, Category

fake = Faker("zh_CN")


def fake_category(count=10):
    """生成假的文章类型"""
    for i in range(count):
        Category.objects.get_or_create(
            name=fake.word()
        )


def fake_article(count=50):
    categorys = Category.objects.values_list('name')
    category_count = Category.objects.count()

    for i in range(count):
        category = categorys[random.randint(0, category_count-1)][0]
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
