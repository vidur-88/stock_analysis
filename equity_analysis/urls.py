from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'all_companies', views.get_all_company_data),
    re_path(r'sector_wise_companies', views.get_sector_wise_data),
    re_path(r'company_data', views.get_company_data),
]
