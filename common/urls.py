from django.urls import path

from common.api_endpoints.MediaFileCreate import MediaFileCreateAPIView
from common.api_endpoints.MediaFileDelete import MediaFileDeleteAPIView

urlpatterns = [
    path("media/create/", MediaFileCreateAPIView.as_view(), name="media-create"),
    path("media/delete/<int:pk>/", MediaFileDeleteAPIView.as_view(), name="media-delete"),
]
