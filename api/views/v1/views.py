from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.auth.securetoken import token_required


@api_view(['head', 'get'])
def health(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['head', 'get'])
@token_required
def health_secure(request):
    return Response(status=status.HTTP_200_OK)