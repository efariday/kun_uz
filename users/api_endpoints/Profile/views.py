from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
# from django.contrib.auth import get_user_model
from users.api_endpoints.Profile.serializers import UserProfileSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @swagger_auto_schema(
        responses={200: UserProfileSerializer()},
        operation_description="Get current user profile"
    )
    def get(self, request):
        # get_user_model() faqat kerak bo‘lgan joyda chaqirilsin
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
