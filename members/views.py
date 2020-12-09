from django.shortcuts import render,redirect
from .models import Members
from .forms import AddMemberForm
from django.urls import reverse


# Create your views here.
def member_list(request):
    member_list = Members.objects.all()
    context = {'members': member_list}
    return render(request, 'members/member_list.html', context)


def add_member(request):
    if request.method == 'POST':
        form = AddMemberForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            n = '10'
            myform.created_by = request.user
            myform.member_no = "AB" + n.zfill(6)
            myform.save()
            return redirect(reverse('members:member_list'))

    else:
        form = AddMemberForm()

    context = {'form': form}
    return render(request, 'members/add_members.html', context)


def member_details(request, slug):
    member_detail = Members.objects.get(slug=slug)
    context = {'member': member_detail}
    return render(request, 'members/member_details.html', context)
