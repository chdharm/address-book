from django.urls import path, re_path
from api.views.v1 import views
from api.controllers.v1.addressbook import add_person, address_book, search_person, delete, edit, add_mobile, add_email, add_address

urlpatterns =[
    path('health/', views.health, name='health'),
    path('addPerson/', add_person, name='add_person'),
    path('addressBook/', address_book, name='address_book'),
    path('searchPerson/', search_person, name='search_person'),
    re_path(r'delete/(?P<pk>[0-9]+$)', delete, name='delete_person_contact'),
    re_path(r'edit/(?P<pk>[0-9]+$)', edit, name='edit_person_contact'),
    re_path(r'addMobile/(?P<pk>[0-9]+$)', add_mobile, name='add_person_mobile'),
    re_path(r'addEmail/(?P<pk>[0-9]+$)', add_email, name='add_person_email'),
    re_path(r'addAddress/(?P<pk>[0-9]+$)', add_address, name='add_person_address'),
]