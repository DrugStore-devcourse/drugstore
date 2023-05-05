from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from ..data_api.models import *
from ..data_collection.models import *
from .constants import *
from django.http import Http404
from django.urls import reverse
from apps.visualization.views import _render_pie_chart
from django.db.models import Sum
import requests
import logging

# Create your views here.
def drug_list(request):
    mosts = []
    context = {}
    try:
        if not Drug.objects.exists() or not Word.objects.exists():
            logging.warning(ROWS_NOT_EXIST)
            context = {'error_message': LIST_CREATION_REJECT}
        else:
            drugs = Drug.objects.all().only('id', 'drfstf', 'drfstf_eng', 'drug_no', 'type_code').values()
            names = [drug['drfstf'] for drug in drugs]
            temps = Word.objects.all().filter(text__in=names)\
                                          .values('text', 'frequency')
            mst_sum = {}
            for temp in temps:
                mst_sum[temp['text']] = mst_sum.get(temp['text'], 0) + temp['frequency']
            mst_tpl = []
            if len(mst_sum) > 10:
                mst_tpl = sorted(mst_sum.items(), key=lambda x:x[1], reverse=True)[:10]
            elif 0 < len(mst_sum) and len(mst_sum) <= 10:
                mst_tpl = sorted(mst_sum.items(), key=lambda x:x[1], reverse=True)
            
            if len(mst_tpl):
                for ele in mst_tpl:
                    mosts.append({'text':ele[0], 'frequency':ele[1]})
    except(Drug.DoesNotExist, Word.DoesNotExist):
        raise Http404("데이터가 없습니다.")
    charts = []
    if len(mosts) == 0:
        logging.warning(DRUGS_NOT_IN_WORDS)
        context['error_message'] = context.get('error_message', LIST_CREATION_FAILED)
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
                    charts.append([drug['drfstf'], most['frequency']])

        context = {'hot_drugs' : hot_drugs}
    try:
        chart_url = "http://" + request.get_host() + reverse('chart:top10_pie_chart')
        if request.get_host() != 'testserver': # test시에는 client의 host가 testserver가 되어 chart/top10의 url 획득 불가능
            context['chart'] = requests.get(chart_url).text
        elif len(charts):
            context['chart'] = _render_pie_chart(charts, 'test')
    except (requests.exceptions.RequestException):
        logging.warning(CHART_LOAD_FAILED)
        context['error_message'] = context.get('error_message', CHART_CREATION_FAILED)

    return render(request, 'web_pages/index.html', context=context)

def drug_detail(request, drug_no):
    drug = get_object_or_404(Drug, drug_no=drug_no)
    return render(request, 'web_pages/detail.html', context={'drug':drug})