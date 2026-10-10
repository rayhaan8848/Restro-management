
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import authentication
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer

User = get_user_model()


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post", "head", "options"]


class LoginView(viewsets.ViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [authentication.TokenAuthentication]

    def create(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)

            return Response({"token": token.key},
                status=status.HTTP_200_OK
            )

        return Response(
            {"message": "Invalid credentials"},
            status=status.HTTP_400_BAD_REQUEST
        )
