#from django.shortcuts import render
from typing import Any
from django import http
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Company
import json

# Create your views here.
class CompanyView(View):

    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0): #Con id=0 -> se listara una compañia 
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {'message':"Success", 'company': company} # Devuelvo un json con un mensaje y con la compañia
            else:
                datos = {'message': "Company not found ..."} # Devuelvo un json con un mensaje si la compañia
            return JsonResponse(datos)            
        else: #Con id=0 -> se listaran todas las compañias 
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {'message':"Success", 'companies': companies} # Devuelvo un json con un mensaje y con las compañias
            else:
                datos = {'message': "Companies not found ..."} # Devuelvo un json con un mensaje sin las compañias
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Company.objects.create(name = jd['name'], website=jd['website'],foundation=jd['foundation'])
        datos = {'message':"Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation =jd['foundation']
            company.save()
            datos = {'message':"Success"} # Devuelvo un json con un mensaje de exito
        else:
            datos = {'message': "Company not found ..."} # Devuelvo un json con un mensaje si la compañia
        return JsonResponse(datos)

    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.filter(id=id).delete()
            datos = {'message':"Success"} # Devuelvo un json con un mensaje de exito
        else:
            datos = {'message': "Company not found ..."} # Devuelvo un json con un mensaje si la compañia
        return JsonResponse(datos)