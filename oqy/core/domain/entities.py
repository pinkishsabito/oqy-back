from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class User:
    id: int
    username: str
    email: str
    password: str

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}


@dataclass(frozen=True)
class Group:
    id: int
    name: str
    managers: list[User]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "managers": [manager.to_dict() for manager in self.managers],
        }


@dataclass(frozen=True)
class Book:
    id: int
    title: str
    author: str
    publication_date: str
    group: Optional[Group] = None

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "publication_date": self.publication_date,
            "group": self.group.to_dict() if self.group else None,
        }


@dataclass(frozen=True)
class BookQuestion:
    id: int
    question_text: str
    book: Optional[Book] = None

    def to_dict(self):
        return {
            "id": self.id,
            "question_text": self.question_text,
            "book": self.book.to_dict() if self.book else None,
        }


@dataclass(frozen=True)
class Forum:
    id: int
    group: Optional[Group] = None

    def to_dict(self):
        return {"id": self.id, "group": self.group.to_dict() if self.group else None}


@dataclass(frozen=True)
class ForumMessage:
    id: int
    sender: User
    forum: Forum
    message_text: str

    def to_dict(self):
        return {
            "id": self.id,
            "sender": self.sender.to_dict(),
            "forum": self.forum.to_dict(),
            "message_text": self.message_text,
        }
