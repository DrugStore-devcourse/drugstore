from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from ..data_api.models import *
from ..data_collection.models import *

# Create your views here.
def drug_list(request):
    drugs = Drug.objects.all().only('id', 'drfstf', 'drfstf_eng').values()
    names = [drug['drfstf'] for drug in drugs]
    if len(Word.objects.all().values()) <= 10:
        mosts = Word.objects.all().filter(text__in=names).order_by('-frequency').values()
    else:
        mosts = Word.objects.all().filter(text__in=names).order_by('-frequency').values()[:10]
    
    hot_drugs = []
    for most in mosts:
        for drug in drugs:
            if drug['drfstf'] == most['text']:
                hot_drugs.append({"id":drug['id'], "drfstf":drug['drfstf'], 'drfstf_eng':drug['drfstf_eng'], 'frequency':most['frequency']})

    context = {'hot_drugs' : hot_drugs}


    return render(request, 'web_pages/index.html', context=context)

def drug_detail(request, drug_id):
    drug = get_object_or_404(Drug, pk=drug_id)
    return render(request, 'web_pages/detail.html', context={'drug':drug})