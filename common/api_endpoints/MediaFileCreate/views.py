from rest_framework.generics import CreateAPIView
from common.models import MediaFile
from common.api_endpoints.MediaFileCreate.serializers import MediaFileCreateSerializer
from drf_yasg.utils import swagger_auto_schema

class MediaFileCreateAPIView(CreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileCreateSerializer

    @swagger_auto_schema(request_body=MediaFileCreateSerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
