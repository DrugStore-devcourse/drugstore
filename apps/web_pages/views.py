from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def hello_view(request):
    # return HttpResponse('<h1>Hola</h1>')
    context = {'hello': 'hola!'}
    return render(request, 'web_pages/index.html', context)
    # return render(request, 'error.html')