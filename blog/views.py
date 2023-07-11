from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import P_serializer, Comment_serializer
from .models import Post, Comment
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from .permissions import AlowUserPermission
# list of all post

class List_of_post_API(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        query_set = Post.objects.all()
        pager = PageNumberPagination()
        result = pager.paginate_queryset(queryset=query_set, request=request)
        serializer = P_serializer(instance=result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# list of posts --> status==true
class List_of_post_true_API(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        query_set = Post.objects.True_status()
        serializer = P_serializer(instance=query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# detail view
class Detail_post_API(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        instance = Post.objects.get(pk=pk)
        serializer = P_serializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
class Add_post_API(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = P_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response({'status': 'added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Update_Delete_post_API(APIView):
    permission_classes = [IsAuthenticated, AlowUserPermission]
    def put(self, request, pk=None):
        instance = Post.objects.get(pk=pk)
        serializer = P_serializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save() # There is an update method inside the save
            return Response({'massage': 'updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)
    def delete(self, request, pk=None):
        instance = Post.objects.get(pk=pk)
        instance.delete()
        return Response({'massage': 'deleted'}, status=status.HTTP_200_OK)

class Add_comment(APIView):

    def post(self, request):
        serializer = Comment_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'massage': 'added comment'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

