from rest_framework import serializers
from .models import Tag, News

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']


class NewsSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    class Meta:
        model = News
        fields = ['id','name', 'content', 'publication_date', 'edition_date', 'tags']

class NewsSerializerOps(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id','name', 'content', 'publication_date', 'edition_date', 'tags']

