from rest_framework import serializers
from .models import UserComment
from apps.users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    """文章评论的序列化函数"""

    user = UserSerializer()

    class Meta:
        model = UserComment
        fields = "__all__"
