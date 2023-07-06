from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Register_serializer
class Register(APIView):
    def post(self, request):
        serializer = Register_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'massage': 'registered'})
        return Response(serializer.errors)
