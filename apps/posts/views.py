from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Post
from .pagination import PostPageNumberPagination
from .renderers import PostJSONRenderer
from .serializers import PostSerializer, PostCreateSerializer


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    renderer_classes = (PostJSONRenderer,)

    def post(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().post(request, *args, **kwargs)


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    pagination_class = PostPageNumberPagination
    renderer_classes = (PostJSONRenderer,)
    filter_backends = [OrderingFilter, ]
    ordering = ['-likes']


class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    renderer_classes = (PostJSONRenderer,)

    def get_object(self, post_pk=0):
        obj = Post.objects.get(pk=post_pk)
        self.check_object_permissions(self.request, obj.author)
        return obj

    def get(self, request, *args, **kwargs):
        instance = self.get_object(post_pk=kwargs.get('pk', None))
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        post_instance = self.get_object(post_pk=kwargs.get('pk', None))
        
        serializer = PostSerializer(
            post_instance, data=request.data, partial=True,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        post_instance = self.get_object(post_pk=kwargs.get('pk', None))
    
        serializer_data = {
            "likes": post_instance.likes + int(request.data.get('likes', 0))
        }
        serializer = PostSerializer(
            post_instance, data=serializer_data,
            partial=True, context={"is_patch": True}
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(post_pk=kwargs.get('pk', None))
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
