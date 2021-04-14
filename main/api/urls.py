from django.urls import path,re_path
from api.views import show_companies,show_company,show_vacancies_of_company,show_vacancies,show_vacancy,show_top,check

urlpatterns = [
    path('companies/', show_companies),
    path('companies/<int:company_id>', show_company),
    path('companies/<int:company_id>/vacancies/', show_vacancies_of_company),
    path('vacancies/', show_vacancies),
    path('vacancies/<int:vacancy_id>', show_vacancy),
    path('vacancies/top_ten/', show_top),
    path('check/', check),
]