from django.urls import path, re_path
from api.views.v1 import views

urlpatterns =[
    path('health/', views.health, name='health'),
    path('addPerson/', , name='add_person'),
    path('searchPerson/', , name='search_person'),
    re_path(r'delete/(?P<pk>[0-9]+$)', , name='delete_person_contact'),
    re_path(r'edit/(?P<pk>[0-9]+$)', , name='edit_person_contact'),
    re_path(r'addMobile/(?P<pk>[0-9]+$)', , name='add_person_mobile'),
    re_path(r'addEmail/(?P<pk>[0-9]+$)', , name='add_person_email'),
    re_path(r'addAddress/(?P<pk>[0-9]+$)', , name='add_person_address'),
]