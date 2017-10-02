from django.http import HttpResponse, HttpResponseServerError
from rest_framework.decorators import api_view
import ujson as json


@api_view(['POST'])
def get_company_data(request):
    try:
        resp = None
    except Exception as e:
        return HttpResponseServerError(json.dumps(
            {
                'Error': 'Server Error',
                'message': e.message
            }
        ))
    return HttpResponse(json.dumps(resp))


@api_view(['POST'])
def get_sectors_list(request):
    try:
        resp = None
    except Exception as e:
        return HttpResponseServerError(json.dumps(
            {
                'Error': 'Server Error',
                'message': e.message
            }
        ))
    return HttpResponse(json.dumps(resp))


@api_view(['POST'])
def get_sector_wise_data(request):
    try:
        resp = None
    except Exception as e:
        return HttpResponseServerError(json.dumps(
            {
                'Error': 'Server Error',
                'message': e.message
            }
        ))
    return HttpResponse(json.dumps(resp))


@api_view(['POST'])
def sort_companies_based_percent_growth(request):
    try:
        resp = None
    except Exception as e:
        return HttpResponseServerError(json.dumps(
            {
                'Error': 'Server Error',
                'message': e.message
            }
        ))
    return HttpResponse(json.dumps(resp))


@api_view(['POST'])
def sort_companies_based_price_diff(request):
    try:
        resp = None
    except Exception as e:
        return HttpResponseServerError(json.dumps(
            {
                'Error': 'Server Error',
                'message': e.message
            }
        ))
    return HttpResponse(json.dumps(resp))
