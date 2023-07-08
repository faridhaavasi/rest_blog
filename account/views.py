from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Register_serializer
from rest_framework import status
class Register(APIView):
    def post(self, request):
        serializer = Register_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'massage': 'registered'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Chek_user(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({'user': user.username}, status=status.HTTP_200_OK)

