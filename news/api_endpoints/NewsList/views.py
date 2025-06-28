from rest_framework.generics import ListAPIView
from news.models import News
from news.api_endpoints.NewsList.serializers import NewsListSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
