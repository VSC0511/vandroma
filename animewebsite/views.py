from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def romance(request):
    return render(request, 'romanceanime.html')

def isekai(request):
    return render(request, 'isekaianime.html')

def shounen(request):
    return render(request, 'shounenanime.html')

def comedy(request):
    return render(request, 'comedyanime.html')

def fantasy(request):
    return render(request, 'fantasyanime.html')