from django.urls import path
from .views import sign_up, customers_list

urlpatterns = [
    path('', sign_up, name='sign_up'),
    path('customers/', customers_list, name='customers_list'),
]