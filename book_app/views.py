from django.shortcuts import render

def home(request):
    return render(request, 'book_app/index.html')
