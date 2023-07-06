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
class List_of_post_true_API(APIView):
    def get(self, request):
        query_set = Post.objects.True_status()
        serializer = P_serializer(instance=query_set, many=True)
        return Response(serializer.data)
# detail view
class Detail_post_API(APIView):
    def get(self, request, pk):
        instance = Post.objects.get(pk=pk)
        serializer = P_serializer(instance=instance)
        return Response(serializer.data)
class Add_post_API(APIView):
    def post(self, request):
        serializer = P_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'added'})
        return Response(serializer.errors)
class Update_post_API(APIView):
    def put(self, request, pk=None):
        instance = Post.objects.get(pk=pk)
        serializer = P_serializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save() # There is an update method inside the save
            return Response({'massage': 'updated'})
        return Response(serializer.errors)


