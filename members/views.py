from django.shortcuts import render
from .models import Members


# Create your views here.
def member_list(request):
    member_list = Members.objects.all()
    context = {'members': member_list}
    return render(request, 'members/member_list.html',context)


def member_details(request, id):
    member_detail = Members.objects.get(id=id)
    context = {'member' : member_detail}
    return render(request,'members/member_details.html',context)
