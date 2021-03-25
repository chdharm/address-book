from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def add_person(request):
    """
    This end point will take the person 
    data and will create their record 
    into the database.

    """
    pass


@api_view(['GET'])
def address_book(request):
    """
    This Endpoint is for getting contact 
    details of all people at a time.
    We will paginate this for 10 items at a time.

    """
    pass

@api_view(['GET'])
def search_person(request):
    """
    This Endpoint is for searching contact 
    details of a person based on their 
    email id or name. 
    We will paginate this for 10 items at a time.

    """
    pass


@api_view(['DELETE'])
def delete(request):
    """
    This Endpoint will delete 
    the person contact details. 
    It expects personId in URL param.

    """
    pass

@api_view(['POST'])
def edit(request):
    """
    This Endpoint will edit the person 
    contact details. 
    It expects personId in URL param.

    """
    pass


@api_view(['PUT'])
def add_mobile(request):
    """
    This Endpoint will add the mobile number 
    into the person contact details. 
    It expects personId in URL param.

    """
    pass

@api_view(['PUT'])
def add_email(request):
    """
    This Endpoint will add the email id into 
    the person contact details. 
    It expects personId in URL param.

    """
    pass

@api_view(['PUT'])
def add_address(request):
    """
    This Endpoint will add the address into 
    the person contact details. 
    It expects personId in URL param.

    """
    pass
