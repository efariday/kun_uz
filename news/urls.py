from django.urls import path

from news.api_endpoints.NewsCreate import NewsCreateAPIView
from news.api_endpoints.NewsList import NewsListAPIView
from news.api_endpoints.NewsDetail import NewsDetailAPIView
from news.api_endpoints.NewsUpdate import NewsUpdateAPIView
from news.api_endpoints.NewsDelete import NewsDeleteAPIView

urlpatterns = [
    path("create/", NewsCreateAPIView.as_view()),
    path("list/", NewsListAPIView.as_view()),
    path("detail/<int:pk>/", NewsDetailAPIView.as_view()),
    path("update/<int:pk>/", NewsUpdateAPIView.as_view()),
    path("delete/<int:pk>/", NewsDeleteAPIView.as_view()),
]
