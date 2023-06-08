from rest_framework.views import APIView
from rest_framework.response import Response
from oqy.core.auth.services import AuthenticationService


class RegisterUserView(APIView):
    def post(self, request) -> JsonResponse:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        authentication_service = AuthenticationService()
        user = authentication_service.register_user(username, email, password)

        return JsonResponse({'message': 'User registered successfully'})


class LoginView(APIView):
    def post(self, request) -> JsonResponse:
        username = request.data.get('username')
        password = request.data.get('password')

        authentication_service = AuthenticationService()
        user = authentication_service.authorize_user(username, password)

        if user:
            return JsonResponse({'message': 'Login successful'})

        return JsonResponse({'message': 'Invalid credentials'}, status=401)
