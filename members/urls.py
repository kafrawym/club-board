from django.urls import path, include
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.member_list,name='member_list'),
    path('adding', views.add_member, name='add_members'),
    path('<str:slug>', views.member_details, name='member_det'),
]
