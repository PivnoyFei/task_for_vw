from parser.models import News, Tag

from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    """Сериализатор тегов."""
    class Meta:
        model = Tag
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор новостей"""
    tags = TagSerializer(read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class NewsCreateSerializer(serializers.ModelSerializer):
    """Сериализатор новостей"""
    tags = serializers.SlugRelatedField(slug_field="name", queryset=Tag.objects.all())

    class Meta:
        model = News
        fields = ('tags', )
