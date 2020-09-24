from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'home.html')

def result(request):

    return render(request, 'result.html')

def book(request):

    return render(request, 'book.html')
def walk(request):

    return render(request, 'walk.html')
def pet(request):

    return render(request, 'pet.html')
def counseling_center(request):

    return render(request, 'counseling_center.html')