from django.urls import path #Nos permite establecer una ruta.
from .views import CompanyView #nos permite inportar la clase CompanyView.

urlpatterns = [
    path ('companies/', CompanyView.as_view(), name='companies_list'),
    path ('companies/<int:id>', CompanyView.as_view(), name='companies_process')
]