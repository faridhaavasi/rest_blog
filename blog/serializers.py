from rest_framework import serializers

# serializer for Post -----> serializers.Serializer

class P_serializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    body = serializers.CharField(max_length=5000)
    status = serializers.BooleanField(required=False)


