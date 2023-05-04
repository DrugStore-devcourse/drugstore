from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from ..data_api.models import *
from ..data_collection.models import *
import requests

# Create your views here.
def drug_list(request):
    drugs = Drug.objects.all().only('id', 'drfstf', 'drfstf_eng', 'drug_no', 'type_code').values()
    names = [drug['drfstf'] for drug in drugs]
    if len(Word.objects.all().values()) <= 10:
        mosts = Word.objects.all().filter(text__in=names).order_by('-frequency').values()
    else:
        mosts = Word.objects.all().filter(text__in=names).order_by('-frequency').values()[:10]
    
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
    context['chart'] = requests.get('http://127.0.0.1:8000/chart/top10').text

    return render(request, 'web_pages/index.html', context=context)

def drug_detail(request, drug_no):
    drug = get_object_or_404(Drug, drug_no=drug_no)
    return render(request, 'web_pages/detail.html', context={'drug':drug})