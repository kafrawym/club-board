import django_filters
from .models import Members


class MembersFilter(django_filters.FilterSet):
    member_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Members
        fields = '__all__'
        exclude = ['member_image', 'slug', 'created_by','created_date']
