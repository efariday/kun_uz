from rest_framework import serializers
from news.models import News


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            "title",
            "slug",
            "content",
            "author",
            "category",
            "tags",
            "default_image",
            "images",
            "is_active",
            "publish_at"
        ]
