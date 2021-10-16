from django.shortcuts import render

def home(request):
    print('home.home')
    return render(request, 'index.html')

