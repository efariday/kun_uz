from rest_framework import serializers
from news.models import News


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "slug", "author", "is_active", "publish_at"]
