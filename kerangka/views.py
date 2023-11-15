from django.shortcuts import render,HttpResponse
from.models import*
# Create your views here.
def mulai(request):
    biodata = Biodata.objects.all()
    return render(request, 'home.html',{"data":biodata})

def home(request):
    return render(request,'halaman2.html')