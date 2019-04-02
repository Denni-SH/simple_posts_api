import copy

from rest_framework.serializers import (
    ModelSerializer, ValidationError,
)
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from .models import User

USER_EXTRA_KWARGS = dict.fromkeys(
    ['_state',
     'is_superuser',
     'is_staff',
     'password',
     'is_active',
     'backend'
     ], {"write_only": True}
)


USER_FIELDS = ['id',
               'username',
               'first_name',
               'last_name',
               'birth_date',
               'phone',
               'email']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = USER_FIELDS
        extra_kwargs = USER_EXTRA_KWARGS


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = list(USER_FIELDS)
        fields.append('password')
        extra_kwargs = USER_EXTRA_KWARGS
        extra_kwargs.update(dict.fromkeys(
            ['password', 'username', 'email'],
            {"required": True}))

    def create(self, request, *args, **kwargs):
        user = User.create(**request)
        user.save()
        return user

    def to_internal_value(self, data):
        if not (
                data.get("password")
                and data.get("username")
                and data.get("email")
        ):
            raise ValidationError(
                {'message': 'Missed one or several required fields!'})
        return super().to_internal_value(data)


class UserLoginSerializer(JSONWebTokenSerializer):

    class Meta(UserSerializer.Meta):
        model = User
        fields = USER_FIELDS.copy()
        extra_kwargs = copy.deepcopy(USER_EXTRA_KWARGS)
        extra_kwargs.update(dict.fromkeys(
            ['password', 'username'],
            {"required": True}))

    def to_internal_value(self, data):
        if not data.get('password') or not data.get('username'):
            raise ValidationError(
                {'message': 'Missed one or several required fields!'})
        return super().to_internal_value(data)
