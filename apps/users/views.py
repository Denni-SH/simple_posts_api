
from rest_framework_jwt.views import ObtainJSONWebToken

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .renderers import (
    LoginJSONRenderer, UserJSONRenderer,
)
from .serializers import (
    UserCreateSerializer, UserLoginSerializer, UserSerializer,
)


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)


class UserLoginView(ObtainJSONWebToken):
    serializer_class = UserLoginSerializer
    renderer_classes = (LoginJSONRenderer,)

    def get(self, request, username=None, *args, **kwargs):
        username_status = True \
            if User.objects.filter(username=username).first() else False
        return Response(
            {'is_reserved': username_status}, status=status.HTTP_200_OK)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    renderer_classes = (UserJSONRenderer,)

    def get_object(self):
        obj = User.objects.get(pk=self.user_pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        self.user_pk = request.user.pk
        return super().get(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if request.data.get('username'):
            request.data.pop('username')
        serializer = UserSerializer(
            request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        self.user_pk = request.user.pk
        return super().delete(self, request, *args, **kwargs)
