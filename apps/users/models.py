from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db.models import DateField, CharField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    birth_date = DateField(null=True, blank=True, default=None)
    phone = CharField(max_length=20, blank=True, default=None, null=True)
    first_name = CharField(
        _('first name'), max_length=30, blank=True, null=True,
    )
    last_name = CharField(
        _('last name'), max_length=150, blank=True, null=True,
    )
    
    @classmethod
    def create(cls, **kwargs):
        new_user = cls()
        new_user.birth_date = kwargs.get('birth_date')
        new_user.email = kwargs.get('email', '')
        new_user.first_name = kwargs.get('first_name')
        new_user.last_name = kwargs.get('last_name')
        new_user.password = make_password(kwargs.get('password'))
        new_user.phone = kwargs.get('phone')
        new_user.username = kwargs.get('username')
        return new_user

    def __str__(self):
        return self.username
