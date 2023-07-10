from rest_framework import serializers
from .models import Post, Comment
from persiantools.jdatetime import JalaliDate, JalaliDateTime

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
    date_ago = serializers.SerializerMethodField()
    #created_as = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_date_ago(self, obj):
        date = obj.created_as
        jalali_date = JalaliDate(date)
        jalali_date_time = JalaliDateTime(jalali_date)
        return jalali_date_time.strftime("%c")

class P_serializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    comments = serializers.SerializerMethodField()
    title = serializers.CharField(max_length=50, validators=[title_forbidden])
    class Meta:
        model = Post
        fields = '__all__'  # all fields serialized
        #exclude = ['id', 'slug', 'created']  # except these fields (these fields should not be serialized)
        validators = [title_forbidden]

    def get_comments(self, obj):
        if obj.comments:
            serializer = Comment_serializer(instance=obj.comments.all(), many=True)
            return serializer.data






