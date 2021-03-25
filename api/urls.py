from django.urls import path, re_path
from . import views

urlpatterns =[
    path('health/', views.health, name='index'),
    re_path(r'____path___/(?P<___id____>[0-9]+$)', ___controller_function_path___, name='___controller__function_alias_name___'),
]