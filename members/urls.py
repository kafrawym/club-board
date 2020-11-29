from django.urls import path, include
from . import views

app_name= 'members'

urlpatterns = [
    path('', views.member_list),
    path('<str:slug>', views.member_details, name='member_det'),
    path('add_members', views.add_members, name='add_members'),
]
