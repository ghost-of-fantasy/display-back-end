"""
对生成假数据的操作进行性能分析

1. 一个一个地插入， 插入5000篇文章 38分钟
2. 批量插入，没有标签，但出现冲突了 41秒
3. 批量插入，没有标签，无视冲突，有冲突的插入失败 43秒
4. 批量插入，有标签 26分钟？？
5. 批量插入，有1标签 26分钟？？25626
6. 使用 postgres， 4分钟

"""

import random
import pytz
from faker import Faker
from apps.news.models import Article

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

