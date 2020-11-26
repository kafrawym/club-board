from django.urls import path, include
from . import views

app_name= 'members'

urlpatterns = [
    path('', views.member_list),
    path('<int:id>', views.member_details, name='member_det'),
]
