from django.db.models import Count
from rest_framework import serializers
from taggit.models import Tag
from .models import Article, Event


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
    tags = serializers.SerializerMethodField()
    stags = serializers.CharField(label="歌单标签的字符串", help_text='中间用空格隔开', write_only=True, required=False)

    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ('tags', )

    def get_tags(self, obj):
        tags = []
        for i in obj.tags.all():
            tag = {'id': i.id, 'name': i.name}
            tags.append(tag)
        return tags

    def update(self, instance, validated_data):
        tags = validated_data.pop('stags', '')
        article = super().update(instance, validated_data)

        if tags:
            article.tags.clear()
            for tag in tags.split(' '):
                article.tags.add(tag)

        return article


class ArticleCreateSerializer(serializers.ModelSerializer):
    """文章创建的序列化函数"""

    title = serializers.CharField(label="文章标题", help_text="文章标题", required=True, allow_blank=False)
    content = serializers.CharField(label="文章内容", help_text="文章内容", required=True, allow_blank=False)
    url = serializers.CharField(label="文章链接", help_text="文章链接", required=True, allow_blank=False)
    tags = serializers.CharField(label="文章标签", help_text="文章标签", required=False)
    website_name = serializers.CharField(label="文章来源网站", required=True)
    publish_time = serializers.DateTimeField(label="发表时间", required=True)

    class Meta:
        model = Article
        fields = ("title", "content", 'url', 'tags', 'website_name', 'publish_time')

    def create(self, validated_data):

        # 添加的时候 假如有 且draft 直接更新
        try:
            item = Article.objects.get(url=validated_data['url'])
            if item.status == 'published':
                raise serializers.ValidationError('已经发布，无法更新')
        except Exception as e:  # 没有这个对象
            if isinstance(e, serializers.ValidationError):
                raise e

        article, created = Article.objects.update_or_create(
            url=validated_data['url'],
            defaults={
                'url': validated_data['url'],
                'title': validated_data['title'],
                'content': validated_data['content'],
                'website_name': validated_data['website_name'],
                'publish_time': validated_data['publish_time'],
            }
        )

        try:
            tags = validated_data['tags']
            for tag in tags.split(' '):
                if tag:
                    article.tags.add(tag)
            article.tags = tags
        except Exception as e:
            article.tags = ""

        return article

class EventDetailSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField(label="游戏新闻列表")

    def get_articles(self, obj):
        return ArticleSerializer(obj.articles, many=True, context={'request': self.context['request']}).data

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ('creator', 'creator', 'id')

class EventListSerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField(label="游戏新闻列表")
    latest = serializers.SerializerMethodField(label="内容")

    def get_articles(self, obj):
        return [{'title':article.title, 'time':article.publish_time} for article in obj.articles.all()]
    
    def get_latest(self, obj):
        return ArticleSerializer(obj.articles.all()[0], context={'request': self.context['request']}).data

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ('creator', )

class EventSerializer(serializers.ModelSerializer):
    """关于游戏新闻事件的序列化函数"""

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ('creator', )

#     def create(self, validated_data):
#         tags = validated_data.pop('stags', '')
#         playlist = super().create(validated_data)
#         playlist.tags.set(get_tag_list(tags))

#         # 记录创建用户
#         user = self.context['request'].myuser
#         playlist.creator = user.username
#         playlist.save()

#         return playlist

#     def update(self, instance, validated_data):
#         tags = validated_data.pop('stags', '')
#         song = validated_data.pop('song', '')

#         playlist = super().update(instance, validated_data)
#         if tags:
#             playlist.tags.set(get_tag_list(tags))
#         if song:
#             try:
#                 playlist.tracks.add(song)
#             except Exception as e:
#                 print("不存在的歌曲：" + song + str(e))

#         return playlist
