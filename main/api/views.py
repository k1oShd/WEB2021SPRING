from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from api.models import Company,Vacancy
from django.db.models import Count
# Create your views here.

def show_companies(request):
    companies = Company.objects.all()
    companies_to_json = [company.to_json() for company in companies]
    return JsonResponse(companies_to_json,safe=False,status=200)
    
def show_company(request, company_id):
    company = Company.objects.get(id=company_id)
    company_to_json = company.to_json()
    return JsonResponse(company_to_json,status=200)

def show_vacancies_of_company(request,company_id):
    vacancies_of_company = Vacancy.objects.filter(company__id=company_id)
    vacancies_of_company_to_json = [vacancy.to_json() for vacancy in vacancies_of_company]
    return JsonResponse(vacancies_of_company_to_json,safe=False,status=200)

def show_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_to_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_to_json,safe=False,status=200)

def show_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    vacancy_to_json = vacancy.to_json()
    return JsonResponse(vacancy_to_json,status=200)

def show_top(request):
    top_ten = Vacancy.objects.values('id','salary').order_by('-salary')[:10]
    top_ten = list(top_ten)
    return JsonResponse(top_ten,safe=False,status=200)

def check(request):
    return HttpResponse('<h1>WEB Application is On-Line and operational...</h1>')