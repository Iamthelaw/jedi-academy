from django.shortcuts import render


def index(request):
    return render(request, 'hr_app/index.html')
