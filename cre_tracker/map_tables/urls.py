from django.urls import path

from . import views

urlpatterns = [
    path('', views.markets_view, name='map_tables'),
    # path('', views.MarketListView.as_view(), name='map_tables'),
]
