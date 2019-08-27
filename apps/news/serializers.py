from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from taggit.models import Tag
from .models import Article, Category, Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """文章类别的序列化函数"""

    class Meta:
        model = Category
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    """文章的序列化函数"""
    category = CategorySerializer()
    tags = serializers.SerializerMethodField('get_tags')

    class Meta:
        model = Article
        fields = "__all__"

    def get_tags(self, obj):
        tags = []
        for i in obj.tags.all():
            tags.append(i.name)
        return tags


class ArticleCreateSerializer(serializers.ModelSerializer):
    """文章创建的序列化函数"""

    title = serializers.CharField(label="文章标题", help_text="文章标题", required=True, allow_blank=False)
    content = serializers.CharField(label="文章内容", help_text="文章内容", required=True, allow_blank=False)
    url = serializers.CharField(label="文章链接", help_text="文章链接", required=True, allow_blank=False,
                                validators=[UniqueValidator(queryset=Article.objects.all(), message="该链接的文章已经存在")])
    tags = serializers.CharField(label="文章标签", help_text="文章标签", required=True)
    website_name = serializers.CharField(label="文章来源网站", required=True)
    publish_time = serializers.DateTimeField(label="发表时间", required=True)

    class Meta:
        model = Article
        fields = ("title", "content", "category", 'url', 'tags', 'website_name', 'publish_time')

    def create(self, validated_data):
        article = Article(
            title=validated_data['title'],
            content=validated_data['content'],
            url=validated_data['url'],
            category=validated_data['category'],
            website_name=validated_data['website_name'],
            publish_time=validated_data['publish_time']
        )
        article.save()
        tags = validated_data['tags']
        for tag in tags.split(' '):
            if tag:
                article.tags.add(tag)
        article.tags = tags

        return article


class CommentSerializer(serializers.ModelSerializer):
    """文章评论的序列化函数"""

    class Meta:
        model = Comment
        fields = "__all__"

    def get_category_name(self, obj):
        category = Category.objects.get(id=obj.category.id)
        serializer = CategorySerializer(category)
        return serializer.data['name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """用户的序列化函数"""

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """用户组的序列化函数"""

    class Meta:
        model = Group
        fields = ['url', 'name']
