import traceback
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response


def token_required(func):
    def _inner(request, *args, **kwargs):
        try:
            token_string = request.META['HTTP_AUTHORIZATION']
            prefix = token_string.split()[0]
            token = token_string.split()[1]
            if prefix == 'Bearer' and token == settings.SECRET_KEY:
                return func(request, *args, **kwargs)
            raise Exception('Token is incorrect')
        except:
            print(traceback.format_exc())
            return Response({'msg': 'INVALID_TOKEN'}, status=status.HTTP_403_FORBIDDEN)

    return _inner
