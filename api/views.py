from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NationalIDSerializer
from rest_framework import status


class DataExtractor(APIView):
    serializer_class = NationalIDSerializer

    def post(self, request):
        serializer = NationalIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
