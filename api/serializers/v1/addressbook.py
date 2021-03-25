from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from api.models import Person, Address, Email, Mobile

class PersonDetailSerializer(serializers.ModelSerializer):

    email = SerializerMethodField()
    mobile = SerializerMethodField()
    address = SerializerMethodField()

    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'email',
            'mobile',
            'address'
        )
    
    def get_email(self, person):
        email = Email.objects.filter(person__id=person.id).last()
        if email:
            email.email
        return None

    def get_mobile(self, person):
        mobile = Mobile.objects.filter(person__id=person.id).last()
        if mobile:
            mobile.mobile
        return None
    
    def get_address(self, person):
        address = Address.objects.filter(person__id=person.id).last()
        if address:
            address.address
        return None