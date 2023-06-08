from django.contrib.auth.backends import BaseBackend
from oqy.core.auth.repositories import get_user_by_username


class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_username(username)
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
