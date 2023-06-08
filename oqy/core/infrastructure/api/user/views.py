from django.http import JsonResponse
from django.views import View

from oqy.core.domain.entities import User
from oqy.core.infrastructure.database.repositories import (
    DjangoUserRepository,
)


class CreateUserView(View):
    def post(self, request) -> JsonResponse:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_repository = DjangoUserRepository()
        user = user_repository.create_user(username, email, password)
        return JsonResponse(
            {"id": user.id, "username": user.username, "email": user.email}
        )


class UserDetailsView(View):
    def get(self, request, user_id) -> JsonResponse:
        user_repository = DjangoUserRepository()
        user = user_repository.get_user_by_id(user_id)

        if not user:
            return JsonResponse({"error": "User not found"}, status=404)
        return JsonResponse(
            {"id": user.id, "username": user.username, "email": user.email}
        )


class UpdateUserView(View):
    def put(self, request, user_id) -> JsonResponse:
        user_repository = DjangoUserRepository()
        user = user_repository.get_user_by_id(user_id)

        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        updated_username = request.POST.get("username")
        updated_email = request.POST.get("email")

        user_repository.update_user(
            User(user.id, updated_username, updated_email, user.password)
        )
        return JsonResponse(
            {"id": user.id, "username": user.username, "email": user.email}
        )


class DeleteUserView(View):
    def delete(self, request, user_id) -> JsonResponse:
        user_repository = DjangoUserRepository()
        user = user_repository.get_user_by_id(user_id)

        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        user_repository.delete_user(user)
        return JsonResponse({"message": "User deleted"})


class UserGroupsView(View):
    def get(self, request, user_id) -> JsonResponse:
        user_repository = DjangoUserRepository()

        user = user_repository.get_user_by_id(user_id)
        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        groups = user_repository.get_user_groups(user)

        group_data = [group.to_dict() for group in groups]

        return JsonResponse({"groups": group_data})
