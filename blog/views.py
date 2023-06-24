from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import P_serializer
from .models import Post


# list of all post

class List_of_post_API(APIView):
    def get(self, request):
        query_set = Post.objects.all()
        serializer = P_serializer(instance=query_set, many=True)
        return Response(serializer.data)

# list of posts --> status==true
