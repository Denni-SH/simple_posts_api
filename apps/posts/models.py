from django.db.models import (
    DateTimeField, CharField, IntegerField,
    TextField, ForeignKey, Model, CASCADE,
)

from posts_api.settings import AUTH_USER_MODEL


class Post(Model):
    title = CharField(
        blank=True, null=False, max_length=20, default='Default_title',
    )
    author = ForeignKey(
        AUTH_USER_MODEL, on_delete=CASCADE, related_name='posts',
    )
    text = TextField()
    timestamp = DateTimeField(auto_now=False, auto_now_add=True)
    likes = IntegerField(default=0)

    def __str__(self):
        return self.title
