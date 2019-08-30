from django.db.models import Count
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from taggit.models import Tag
from .models import Article


class TagSerializer(serializers.ModelSerializer):
    num_times = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = "__all__"

    def get_num_times(self, obj):
        queryset = Tag.objects.filter(name=obj.name)
        tags = queryset.annotate(num_times=Count('taggit_taggeditem_items'))

        return tags[0].num_times


class ArticleSerializer(serializers.ModelSerializer):
    """文章的序列化函数"""
    tags = serializers.SerializerMethodField('get_tags')

    class Meta:
        model = Article
        fields = "__all__"

    def get_tags(self, obj):
        tags = []
        for i in obj.tags.all():
            tag = {'id': i.id, 'name': i.name}
            tags.append(tag)
        return tags


class ArticleCreateSerializer(serializers.ModelSerializer):
    """文章创建的序列化函数"""

    title = serializers.CharField(label="文章标题", help_text="文章标题", required=True, allow_blank=False)
    content = serializers.CharField(label="文章内容", help_text="文章内容", required=True, allow_blank=False)
    url = serializers.CharField(label="文章链接", help_text="文章链接", required=True, allow_blank=False,
                                validators=[UniqueValidator(queryset=Article.objects.all(), message="该链接的文章已经存在")])
    tags = serializers.CharField(label="文章标签", help_text="文章标签", required=False)
    website_name = serializers.CharField(label="文章来源网站", required=True)
    publish_time = serializers.DateTimeField(label="发表时间", required=True)

    class Meta:
        model = Article
        fields = ("title", "content", 'url', 'tags', 'website_name', 'publish_time')

    def create(self, validated_data):
        article = Article(
            title=validated_data['title'],
            content=validated_data['content'],
            url=validated_data['url'],
            website_name=validated_data['website_name'],
            publish_time=validated_data['publish_time']
        )
        article.save()
        try:
            tags = validated_data['tags']
            for tag in tags.split(' '):
                if tag:
                    article.tags.add(tag)
            article.tags = tags
        except Exception as e:
            article.tags = ""

        return article


