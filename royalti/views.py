from django.shortcuts import render

# Create your views here.
def list_royalti(request):
    return render(request, 'list_royalti.html')