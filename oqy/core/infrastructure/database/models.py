from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class ModelUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    groups = models.ManyToManyField('auth.Group', related_name='auth_user')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='auth_user')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    class Meta:
        managed = True
        db_table = 'users'


class ModelGroup(models.Model):
    name = models.CharField(max_length=255)
    managers = models.ManyToManyField(ModelUser, related_name="managed_groups")
    book = models.OneToOneField("ModelBook", on_delete=models.CASCADE)
    forum = models.OneToOneField("ModelForum", on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "groups"


class ModelBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()

    class Meta:
        managed = True
        db_table = "books"


class ModelBookQuestion(models.Model):
    question_text = models.TextField()
    book = models.ForeignKey(ModelBook, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "book_questions"


class ModelForum(models.Model):
    group = models.OneToOneField(ModelGroup, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "forums"


class ModelForumMessage(models.Model):
    sender = models.ForeignKey(ModelUser, on_delete=models.CASCADE)
    forum = models.ForeignKey(ModelForum, on_delete=models.CASCADE)
    message_text = models.TextField()

    class Meta:
        managed = True
        db_table = "forum_messages"
