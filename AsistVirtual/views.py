from .onnx_inference import generate_suggestion
from django.shortcuts import render
from .forms import inputAsist

# Create your views here.
def Asist_Virtual(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'form':inputAsist(), 'response':''})
    elif request.method == 'POST':
        response = generate_suggestion(request.POST['input'])
        return render(request, 'index.html', {'form':inputAsist(), 'response':response.content})