from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'all_companies', views.get_all_company_data),
    url(r'company_data', views.get_company_data),
]
