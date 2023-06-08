from django.http import JsonResponse
from oqy.core.auth.services import authorize_user


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if authorize_user(username, password):
            return JsonResponse({"message": "Login successful"})

        return JsonResponse({"message": "Invalid credentials"}, status=401)
