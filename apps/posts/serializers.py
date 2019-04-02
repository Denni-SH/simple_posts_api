from rest_framework.serializers import ModelSerializer

from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get("context")
        self.is_patch = context.get("is_patch", False) if context else False

    def update(self, instance, validated_data):
        if not self.is_patch and validated_data.get("likes"):
            del validated_data["likes"]
        return super().update(instance, validated_data)


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('likes',)
        extra_kwargs = {
            "title": {"required": True},
            "text": {"required": True},
        }
