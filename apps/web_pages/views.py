from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from ..data_api.models import *
from ..data_collection.models import *
from .constants import *
from django.http import Http404
from django.urls import reverse
import requests
import logging

# Create your views here.
def drug_list(request):
    try:
        if not Drug.objects.exists() or not Word.objects.exists():
            logging.warning(ROWS_NOT_EXIST)
            context = {'error_message': LIST_CREATION_REJECT}
        else:

            drugs = Drug.objects.all().only('id', 'drfstf', 'drfstf_eng', 'drug_no', 'type_code').values()
            names = [drug['drfstf'] for drug in drugs]
            if len(Word.objects.all().values()) <= 10:
                mosts = Word.objects.all().filter(text__in=names).order_by('-frequency').values()
            else:
                mosts = Word.objects.all().filter(text__in=names).order_by('-frequency').values()[:10]
    except(Drug.DoesNotExist, Word.DoesNotExist):
        raise Http404("데이터가 없습니다.")

    if len(mosts) == 0:
        logging.warning(DRUGS_NOT_IN_WORDS)
        context = {'error_message': LIST_CREATION_FAILED}
    else:
        hot_drugs = []
        for most in mosts:
            for drug in drugs:
                if drug['drfstf'] == most['text']:
                    hot_drugs.append({"id":drug['id'], 
                                    "drfstf":drug['drfstf'], 
                                    'drfstf_eng':drug['drfstf_eng'], 
                                    'type_code':drug['type_code'],
                                    'frequency':most['frequency'], 
                                    'drug_no':drug['drug_no']})

        context = {'hot_drugs' : hot_drugs}
    try:
        
        chart_url = "http://" + request.get_host() + reverse('chart:top10_pie_chart')
        context['chart'] = requests.get(chart_url).text
    except (requests.exceptions.RequestException):
        logging.warning(CHART_LOAD_FAILED)
        context = {'error_message': CHART_CREATION_FAILED}

    return render(request, 'web_pages/index.html', context=context)

def drug_detail(request, drug_no):
    drug = get_object_or_404(Drug, drug_no=drug_no)
    return render(request, 'web_pages/detail.html', context={'drug':drug})