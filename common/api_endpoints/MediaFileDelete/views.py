from rest_framework.generics import DestroyAPIView
from common.models import MediaFile
from common.api_endpoints.MediaFileDelete.serializers import MediaFileDeleteSerializer
from drf_yasg.utils import swagger_auto_schema

class MediaFileDeleteAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileDeleteSerializer

    @swagger_auto_schema(request_body=MediaFileDeleteSerializer)
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
