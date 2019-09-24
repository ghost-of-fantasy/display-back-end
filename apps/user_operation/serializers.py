from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserComment, UserFav
from apps.users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    """文章评论的序列化函数"""

    user = UserSerializer()

    class Meta:
        model = UserComment
        fields = "__all__"


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
