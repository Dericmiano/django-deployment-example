from django.shortcuts import render


def index(request):
    return render(request, 'slider.html')

# Create your views here.
