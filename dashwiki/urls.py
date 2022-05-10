from django.urls import path
from .views import list_dashpages, list_dashcollections, list_dashpages_by_collection

urlpatterns = [
    # path('', list_dashpages, name='list_dashpages'),
    path('list-collections', list_dashcollections, name='list_dashcollections'),
    path('list-dashpages', list_dashpages, name='list_dashpages'),
    path('list-dashpages-by-collection/<int:id>', list_dashpages_by_collection, name='list_dashpages_by_collection')

]
