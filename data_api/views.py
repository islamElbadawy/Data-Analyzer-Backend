
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Data
from .serializers import DataSerializer
from .utils import *


@api_view(['POST'])
def process_data(request):

    data_list = request.data.get('dataset', [])
    
    processed_data = analyze(data_list)

    return Response(data=processed_data, status=status.HTTP_201_CREATED)
    




