from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {}) # ovde moze da ide dictionery


def about(request):
    return render(request, 'about.html', {})