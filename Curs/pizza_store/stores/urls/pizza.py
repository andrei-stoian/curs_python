from django.urls import path
from stores.views.pizza import list_view, add_to_cart, PizzaList


app_name = 'pizza'

urlpatterns = [
    path('', list_view, name='list'),
    path('<int:pizza_id>/', PizzaList.as_view(), name='details'),
    path('<int:pizza_id>/add_to_cart/', add_to_cart, name='add_to_cart'),
]
