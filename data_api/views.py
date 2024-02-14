

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Person
from .serializers import DataSerializer

class DataCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = DataSerializer

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def add_product(request):
        data = request.data
        print(data)
        serializer = DataSerializer(data = data)
        if serializer.is_valid():
            product = Product.objects.create(**data, user = request.user)
            res = ProductSerializer(product, many=False)
            return Response(res.data)
        else:
            return Response(serializer.errors)


