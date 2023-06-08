from django.http import JsonResponse
from django.views import View
from django_ratelimit.decorators import ratelimit

from oqy.core.domain.entities import Group, ForumMessage
from oqy.core.domain.repositories import (
    GroupRepository,
    UserRepository,
    ForumRepository,
)
from oqy.core.infrastructure.database.repositories import (
    DjangoUserRepository,
    DjangoGroupRepository,
    DjangoForumRepository,
)


class GroupCreateView(View):
    @ratelimit(key='ip', rate='5/s')
    def post(self, request) -> JsonResponse:
        name = request.POST.get("name")
        group_repository: GroupRepository = DjangoGroupRepository()
        group = group_repository.create_group(name)
        return JsonResponse({"group_id": group.id})


class GroupDetailView(View):
    @ratelimit(key='ip', rate='5/s')
    def get(self, request, pk) -> JsonResponse:
        group_repository: GroupRepository = DjangoGroupRepository()
        group = group_repository.get_group(pk)
        if group:
            return JsonResponse({"group_id": group.id, "name": group.name})
        return JsonResponse({"error": "Group not found"}, status=404)


class GroupUpdateView(View):
    @ratelimit(key='ip', rate='5/s')
    def put(self, request, pk) -> JsonResponse:
        name = request.PUT.get("name")
        group_repository: GroupRepository = DjangoGroupRepository()
        group = group_repository.get_group(pk)
        if group:
            group_repository.update_group(Group(group.id, name, group.managers))
            return JsonResponse({"success": "Group updated successfully"})
        return JsonResponse({"error": "Group not found"}, status=404)


class GroupDeleteView(View):
    @ratelimit(key='ip', rate='5/s')
    def delete(self, request, pk) -> JsonResponse:
        group_repository: GroupRepository = DjangoGroupRepository()
        group = group_repository.get_group(pk)
        if group:
            group_repository.delete_group(group)
            return JsonResponse({"success": "Group deleted successfully"})
        return JsonResponse({"error": "Group not found"}, status=404)


class ManagerAddView(View):
    @ratelimit(key='ip', rate='5/s')
    def post(self, request, pk) -> JsonResponse:
        group_repository: GroupRepository = DjangoGroupRepository()
        user_repository: UserRepository = DjangoUserRepository()

        group = group_repository.get_group(pk)
        if not group:
            return JsonResponse({"error": "Group not found"}, status=404)

        username = request.POST.get("username")
        user = user_repository.get_user_by_username(username)
        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        group_repository.add_manager(group, user)
        return JsonResponse({"success": "Manager added successfully"})


class ManagerRemoveView(View):
    @ratelimit(key='ip', rate='5/s')
    def delete(self, request, group_pk, manager_pk) -> JsonResponse:
        group_repository: GroupRepository = DjangoGroupRepository()
        user_repository: UserRepository = DjangoUserRepository()

        group = group_repository.get_group(group_pk)
        if not group:
            return JsonResponse({"error": "Group not found"}, status=404)

        manager = user_repository.get_user_by_id(manager_pk)
        if not manager:
            return JsonResponse({"error": "Manager not found"}, status=404)

        group_repository.remove_manager(group, manager)
        return JsonResponse({"success": "Manager removed successfully"})


class ForumDetailView(View):
    @ratelimit(key='ip', rate='5/s')
    def get(self, request, group_id) -> JsonResponse:
        group_repository: GroupRepository = DjangoGroupRepository()
        forum_repository: ForumRepository = DjangoForumRepository()

        group = group_repository.get_group(group_id)
        if group is None:
            return JsonResponse({"error": "Invalid group ID"}, status=400)

        forum = forum_repository.get_forum(group_id)
        if forum is None:
            return JsonResponse({"error": "Forum not found"}, status=404)

        return JsonResponse(forum.to_dict(), status=200)


class ForumMessageCreateView(View):
    @ratelimit(key='ip', rate='5/s')
    def post(self, request, group_id) -> JsonResponse:
        user_repository: UserRepository = DjangoUserRepository()
        group_repository: GroupRepository = DjangoGroupRepository()
        forum_repository: ForumRepository = DjangoForumRepository()

        user_id = request.POST.get("user_id")
        message_text = request.POST.get("message_text")

        user = user_repository.get_user_by_id(user_id)
        if user is None:
            return JsonResponse({"error": "User not found"}, status=404)

        group = group_repository.get_group(group_id)
        if group is None:
            return JsonResponse({"error": "Group not found"}, status=404)

        forum = forum_repository.get_forum(group_id)
        if forum is None:
            return JsonResponse({"error": "Forum not found"}, status=404)

        message = forum_repository.create_message(user, forum, message_text)
        return JsonResponse(message.to_dict(), status=201)


class ForumMessageDetailView(View):
    @ratelimit(key='ip', rate='5/s')
    def get(self, request, group_id, message_id) -> JsonResponse:
        forum_repository: ForumRepository = DjangoForumRepository()

        forum = forum_repository.get_forum(group_id)
        if forum is None:
            return JsonResponse({"error": "Forum not found"}, status=404)

        messages = forum_repository.get_messages(forum)
        message = next((m for m in messages if m.id == message_id), None)
        if message is None:
            return JsonResponse({"error": "Message not found"}, status=404)

        return JsonResponse(message.to_dict(), status=200)


class ForumMessageUpdateView(View):
    @ratelimit(key='ip', rate='5/s')
    def put(self, request, group_id, message_id) -> JsonResponse:
        message_text = request.POST.get("message_text")

        forum_repository: ForumRepository = DjangoForumRepository()

        forum = forum_repository.get_forum(group_id)
        if forum is None:
            return JsonResponse({"error": "Forum not found"}, status=404)

        messages = forum_repository.get_messages(forum)
        message = next((m for m in messages if m.id == message_id), None)
        if message is None:
            return JsonResponse({"error": "Message not found"}, status=404)

        forum_repository.update_message(
            ForumMessage(message.id, message.sender, message.forum, message_text)
        )

        return JsonResponse(message.to_dict(), status=200)


class ForumMessageDeleteView(View):
    @ratelimit(key='ip', rate='5/s')
    def delete(self, request, group_id, message_id) -> JsonResponse:
        forum_repository: ForumRepository = DjangoForumRepository()

        forum = forum_repository.get_forum(group_id)
        if forum is None:
            return JsonResponse({"error": "Forum not found"}, status=404)

        messages = forum_repository.get_messages(forum)
        message = next((m for m in messages if m.id == message_id), None)
        if message is None:
            return JsonResponse({"error": "Message not found"}, status=404)

        forum_repository.delete_message(message)

        return JsonResponse({"message": "Message deleted"}, status=200)
