from django import forms
from .models import Members


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['first_name', 'middle_name', 'last_name', 'id_no', 'date_of_birth', 'member_type', 'gender',
                  'member_image']
