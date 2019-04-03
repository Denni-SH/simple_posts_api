import clearbit
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken

from .models import User
from .renderers import LoginJSONRenderer, UserJSONRenderer
from .serializers import (
    UserCreateSerializer, UserLoginSerializer, UserSerializer,
)


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    
    @staticmethod
    def check_request_for_extra_info(request):
        user_email = request.data.get("email")
        from django.conf import settings

        if settings.TESTING:
            request.data._mutable = True
        if user_email:
            response = clearbit.Enrichment.find(email=user_email, stream=True)
            fields = ["avatar", "facebook", "twitter", "linkedin", "github"]
            for field in fields:
                person_info = dict(response).get("person")
                if person_info and person_info.get(field):
                    if field != 'avatar':
                        request.data[field] = str(
                            person_info[field].get("handle"),
                        ) if person_info[field].get("handle") else None
                    else:
                        request.data["avatar"] = str(person_info["avatar"]) \
                            if person_info["avatar"] else None
        return request
    
    def get(self, request, username=None, *args, **kwargs):
        username_status = True \
            if User.objects.filter(username=username).first() else False
        return Response(
            {'is_reserved': username_status}, status=status.HTTP_200_OK,
        )
    
    def post(self, request, *args, **kwargs):
        request = self.check_request_for_extra_info(request)
        return super().post(request, *args, **kwargs)


class UserLoginView(ObtainJSONWebToken):
    serializer_class = UserLoginSerializer
    renderer_classes = (LoginJSONRenderer,)


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
            request.user, data=request.data, partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        self.user_pk = request.user.pk
        return super().delete(self, request, *args, **kwargs)
