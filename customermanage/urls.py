from django.urls import path
from .views import SearchResultsView

from .views import index
from .views import create


urlpatterns = [
    path('', index, name='index'),
    path('search/', SearchResultsView, name='search_results'),
    path('create/',create ,name="create")
   ]