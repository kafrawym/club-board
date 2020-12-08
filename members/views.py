from django.shortcuts import render
from .models import Members
from .forms import AddMemberForm


# Create your views here.
def member_list(request):
    member_list = Members.objects.all()

    if request.method == 'POST':
        form = AddMemberForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            n = chr(myform.id)
            myform.member_no = "AB" + n.zfill(6)
            myform.member_name = myform.first_name + ' ' + myform.middle_name + ' ' + myform.last_name
            myform.slug = '9875' + chr(myform.id) + '1245'

    else:
        form = AddMemberForm()

    context = {'members': member_list, 'form':form}
    return render(request, 'members/member_list.html', context)


def member_details(request, slug):
    member_detail = Members.objects.get(slug=slug)
    context = {'member': member_detail}
    return render(request, 'members/member_details.html', context)
