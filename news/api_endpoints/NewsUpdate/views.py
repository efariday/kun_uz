from rest_framework.generics import UpdateAPIView
from news.models import News
from news.api_endpoints.NewsUpdate.serializers import NewsUpdateSerializer
from drf_yasg.utils import swagger_auto_schema

class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsUpdateSerializer

    @swagger_auto_schema()
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
