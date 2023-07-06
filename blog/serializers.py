from rest_framework import serializers
from .models import Post
# serializer for Post -----> serializers.Serializer

# class P_serializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     body = serializers.CharField(max_length=5000)
#     status = serializers.BooleanField(required=False)
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#

# serializer P_serializer ------> serializer.ModelSerializer

class P_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'  # all fields serialized
        exclude = ['id', 'slug', 'created']  # except these fields (these fields should not be serialized)


