from django.shortcuts import render

# Create your views here.
def list_royalti(request):
    context={}
    context["user"] = dict(request.session)
    return render(request, 'list_royalti.html',context=context)