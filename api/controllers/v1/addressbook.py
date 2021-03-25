import traceback
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Person, Address, Email, Mobile
from api.serializers.v1.addressbook import PersonDetailSerializer


@api_view(['POST'])
def add_person(request):
    """
    This end point will take the person 
    data and will create their record 
    into the database.

    """
    try:
        request_data = request.data

        name = request_data.get("name")
        mobile = request_data.get("mobile")
        email = request_data.get("email")
        address = request_data.get("address")

        person = Person.objects.create(name=name)

        if mobile:
            Mobile.objects.create(
                mobile=mobile,
                person_id=person.id
            )
        if email:
            Email.objects.create(
                email=email,
                person_id=person.id
            )
        if address:
            Address.objects.create(
                address=address,
                person_id=person.id
            )
        serializer = PersonDetailSerializer(person)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        print(traceback.format_exc())
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def address_book(request):
    """
    This Endpoint is for getting contact 
    details of all people at a time.
    We will paginate this for 10 items at a time.

    """
    try:
        persons = Person.objects.all()
        serializer = PersonDetailSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        print(traceback.format_exc())
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def search_person(request):
    """
    This Endpoint is for searching contact 
    details of a person based on their 
    email id or name. 
    We will paginate this for 10 items at a time.

    """

    request.GET.get("analyst_id")
    pass


@api_view(['DELETE'])
def delete(request):
    """
    This Endpoint will delete 
    the person contact details. 
    It expects personId in URL param.

    """

    request_data = request.data
    pass


@api_view(['POST'])
def edit(request):
    """
    This Endpoint will edit the person 
    contact details. 
    It expects personId in URL param.

    """

    request_data = request.data
    pass


@api_view(['PUT'])
def add_mobile(request):
    """
    This Endpoint will add the mobile number 
    into the person contact details. 
    It expects personId in URL param.

    """

    request_data = request.data
    pass


@api_view(['PUT'])
def add_email(request):
    """
    This Endpoint will add the email id into 
    the person contact details. 
    It expects personId in URL param.

    """

    request_data = request.data
    pass


@api_view(['PUT'])
def add_address(request):
    """
    This Endpoint will add the address into 
    the person contact details. 
    It expects personId in URL param.

    """

    request_data = request.data
    pass
