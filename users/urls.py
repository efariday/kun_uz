# users/urls.py

from django.urls import path

from users.api_endpoints.LoginSession.views import LoginSessionAPIView
from users.api_endpoints.LogoutSession.views import LogoutSessionAPIView
from users.api_endpoints.Register.views import RegisterAPIView, RegisterConfirmAPIView
from users.api_endpoints.Profile.views import ProfileAPIView

app_name = "users"

urlpatterns = [
    path('login/', LoginSessionAPIView.as_view(), name='login'),
    path('logout/', LogoutSessionAPIView.as_view(), name='logout'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('confirm-email/', RegisterConfirmAPIView.as_view(), name='confirm-email'),
]
