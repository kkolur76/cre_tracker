import django_tables2 as tables
from .models import Unemployment, Population, JobDiversity, MedianRent, RentalVacancy


class MarketTable(tables.Table):
    msa = tables.Column(accessor='unemployment.msa')
    msa_name = tables.Column(accessor='unemployment.msa_name')
    total_ppl = tables.Column(accessor='population.total_ppl')
    unemployed_pe = tables.Column(accessor='unemployment.unemployed_pe')

    class Meta:
        model = Unemployment
        template_name = "django_tables2/bootstrap4.html"

