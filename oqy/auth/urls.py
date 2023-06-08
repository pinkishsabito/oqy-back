from django.urls import path
from oqy.auth.views import login

urlpatterns = [
    path("login/", login, name="auth-login"),
]
