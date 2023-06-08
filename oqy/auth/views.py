from rest_framework.views import APIView
from oqy.core.application.auth.services import AuthenticationService


class RegisterUserView(APIView):
    def post(self, request) -> JsonResponse:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        user_repository = DjangoUserRepository()
        authentication_service = AuthenticationService(user_repository)
        user = authentication_service.register_user(username, email, password)

        return JsonResponse({'message': 'User registered successfully'})


class LoginView(APIView):
    def post(self, request) -> JsonResponse:
        username = request.data.get('username')
        password = request.data.get('password')

        user_repository = DjangoUserRepository()
        authentication_service = AuthenticationService(user_repository)
        user = authentication_service.authorize_user(username, password)

        if user:
            return JsonResponse({'message': 'Login successful'})

        return JsonResponse({'message': 'Invalid credentials'}, status=401)
