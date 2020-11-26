from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.member_list),
    path('<int:id>',views.member_details),
]