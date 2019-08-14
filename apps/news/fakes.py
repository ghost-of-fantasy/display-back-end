import pytz
from faker import Faker
from apps.news.models import Article

fake = Faker()


def fake_article(count=50):
    for i in range(count):
        Article.objects.get_or_create(
            website_name=fake.name(),  # 来源网站的名称
            url=fake.sentence(),  # 文章链接
            title=fake.sentence(),  # 文章标题
            content=fake.text(2000),  # 文章内容
            category=fake.sentence(),  # 文章类型
            publish_time=fake.date_time_this_year(tzinfo=pytz.UTC)
        )
