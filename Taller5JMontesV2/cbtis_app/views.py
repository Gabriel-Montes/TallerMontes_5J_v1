from django.shortcuts import render # type: ignore
from cbtis_app import urls
# Create your views here.
def listView(request):
    return render(request,'index.html')