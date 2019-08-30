import random
import pytz
from faker import Faker
from apps.news.models import Article
from apps.users.models import UserProfile
from apps.user_operation.models import UserFav, UserComment

fake = Faker("zh_CN")


def fake_comment(count=500):
    """生成假评论数据的函数"""
    articles = Article.objects.values_list('id')
    articles_count = Article.objects.count()
    users = UserProfile.objects.values_list('id')
    users_count = UserProfile.objects.count()

    for i in range(count):
        article_id = articles[random.randint(0, articles_count - 1)][0]
        user_id = users[random.randint(0, users_count - 1)][0]
        try:
            UserComment.objects.get_or_create(
                article=Article.objects.get(id=article_id),
                user=UserProfile.objects.get(id=user_id),
                body=fake.text(100),  # 文章标题
                created=fake.date_time_this_year(tzinfo=pytz.UTC)
            )
        except Exception as e:
            print(e)

