from rest_framework.generics import CreateAPIView
from news.models import News
from news.api_endpoints.NewsCreate.serializers import NewsCreateSerializer
from drf_yasg.utils import swagger_auto_schema

class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer

    @swagger_auto_schema(request_body=NewsCreateSerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
