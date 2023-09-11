import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    issued_date__lte = django_filters.DateFilter(field_name='issued_date', lookup_expr='lte')
    issued_date__gte = django_filters.DateFilter(field_name='issued_date', lookup_expr='gte')
    expire_date__lte = django_filters.DateFilter(field_name='expire_date', lookup_expr='lte')
    expire_date__gte = django_filters.DateFilter(field_name='expire_date', lookup_expr='gte')

    class Meta:
        model = Task
        fields = {
            'theme': ['exact', 'icontains'],
            'subject__title': ['icontains'],
            'given_by__full_name': ['exact'],
        }
