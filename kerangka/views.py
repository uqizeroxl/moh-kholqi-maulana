from django.shortcuts import render,HttpResponse

# Create your views here.
def mulai(request):
    return render(request, 'home.html')

def home(request):
    return render(request,'halaman2.html')