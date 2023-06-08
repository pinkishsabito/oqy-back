from django.urls import path
from oqy.auth.views import RegisterUserView, LoginView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='auth-register'),
    path('login/', LoginView.as_view(), name='auth-login'),
]
