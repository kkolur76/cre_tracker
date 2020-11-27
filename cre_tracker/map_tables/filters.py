import django_filters

from .models import *


class MarketsFilter(django_filters.FilterSet):
    class Meta:
        model = Unemployment
        fields = '__all__'

