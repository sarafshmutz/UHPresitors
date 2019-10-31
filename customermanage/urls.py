from django.urls import path
from .views import SearchResultsView

from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('search/', SearchResultsView, name='search_results'),

   ]