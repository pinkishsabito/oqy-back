from django.http import JsonResponse
from django_ratelimit.decorators import ratelimit
from rest_framework.views import APIView

from oqy.auth.services import AuthenticationService
from oqy.core.infrastructure.database.repositories import DjangoUserRepository


class RegisterUserView(APIView):
    @ratelimit(key='ip', rate='2/s')
    def post(self, request) -> JsonResponse:
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        user_repository = DjangoUserRepository()
        authentication_service = AuthenticationService(user_repository)
        authentication_service.register_user(username, email, password)

        return JsonResponse({"message": "User registered successfully"})


class LoginView(APIView):
    @ratelimit(key='ip', rate='5/m')
    def post(self, request) -> JsonResponse:
        username = request.data.get("username")
        password = request.data.get("password")

        user_repository = DjangoUserRepository()
        authentication_service = AuthenticationService(user_repository)
        user = authentication_service.authorize_user(username, password)

        if user:
            return JsonResponse({"message": "Login successful"})

        return JsonResponse({"message": "Invalid credentials"}, status=401)
