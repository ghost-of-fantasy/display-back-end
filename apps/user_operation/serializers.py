from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav
from apps.users.serializers import UserSerializer


class UserFavSerializer(serializers.ModelSerializer):
    """用户收藏的序列化函数"""

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav

        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'article'),
                message="已经收藏"
            )
        ]

        fields = ('user', 'article', 'id')
