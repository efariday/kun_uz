from rest_framework.generics import RetrieveAPIView
from news.models import News
from news.api_endpoints.NewsDetail.serializers import NewsDetailSerializer
from drf_yasg.utils import swagger_auto_schema

class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
