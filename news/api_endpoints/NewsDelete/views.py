from rest_framework.generics import DestroyAPIView
from news.models import News
from news.api_endpoints.NewsDelete.serializers import NewsDeleteSerializer
from drf_yasg.utils import swagger_auto_schema

class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDeleteSerializer

    @swagger_auto_schema(request_body=NewsDeleteSerializer)
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
