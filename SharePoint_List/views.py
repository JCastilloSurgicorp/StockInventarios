from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def SharePoint_List(request):
    return render(request, 'web/index.html')                               