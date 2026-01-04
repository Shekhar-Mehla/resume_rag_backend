

# Create your views here.
from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import status
from .serializer import ResumeSerializer


class ResumeView(APIView):
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            # Process the resume data
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)