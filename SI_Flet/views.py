from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def SI_Flet(request):
    return render(request, 'fletwithSQL/xref-fletwithSQL.html')                               