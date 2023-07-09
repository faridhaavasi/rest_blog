from rest_framework import serializers
from .models import Post, Comment
# serializer for Post -----> serializers.Serializer

# class P_serializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     body = serializers.CharField(max_length=5000)
#     status = serializers.BooleanField(required=False)
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#

# serializer P_serializer ------> serializer.ModelSerializer
# fun validator
def title_forbidden(data):
    list_of_title_forbidden = ['alexis', 'alexis texas', 'porn', 'johny', 'johny sins', 'porno', 'sex']
    if data in list_of_title_forbidden:
        raise serializers.ValidationError({'title': 'Shame on you:/ Inaccurate vulgarity'})
    for i in list_of_title_forbidden:
        if data == i.upper():
            raise serializers.ValidationError('Shame on you:/ Inaccurate vulgarity')
        if data == i:
            raise serializers.ValidationError('Shame on you:/ Inaccurate vulgarity')
class Comment_serializer(serializers.ModelSerializer):
    #created_as = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'
class P_serializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    title = serializers.CharField(max_length=50, validators=[title_forbidden])
    class Meta:
        model = Post
        #fields = '__all__'  # all fields serialized
        exclude = ['id', 'slug', 'created']  # except these fields (these fields should not be serialized)
        validators = [title_forbidden]

    def get_comments(self, obj):
        serializer = Comment_serializer(instance=obj.comments.all(), many=True)
        return serializer.data




