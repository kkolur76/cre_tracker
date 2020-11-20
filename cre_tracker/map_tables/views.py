from django.shortcuts import render
from django.http import HttpResponse
from .models import Unemployment, Population, JobDiversity, RentalVacancy, MedianRent


def index(request):
    return HttpResponse("Hello, World!")


def markets_view(request):
    # pass
    markets_unemployment = Unemployment.objects.all()
    markets_population = Population.objects.all()
    markets_job_diversity = JobDiversity.objects.all()
    markets_vacancy_rate = RentalVacancy.objects.all()
    markets_median_rent = MedianRent.objects.all()

    markets_info = zip(Population.objects.all(), JobDiversity.objects.all(),
                       RentalVacancy.objects.all(), MedianRent.objects.all())
    cols = ['MSA_ID', 'MSA_Name', 'Total Pop.', 'Unemployed %', 'Median Rent $', 'Vacancy Rent %',
            '<5', '5-9', '10-14', '15-19', '20-24', '25-34', '35-44', '45-54', '55-59', '60-64', '65-74', '75-84',
            '>85', 'AGC %', 'CSTN %', 'MFG %', 'WHLS %', 'RTL %', 'TSPT %', 'IT %', 'BUS. %', 'SCI %', 'EDU %', 'ENT %',
            'OTHER %', 'P. ADM %']
    context = {'markets': markets_info, 'cols': cols}

    # pdb.set_trace()
    return render(request, "map_tables.html", context)
