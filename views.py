from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    context = {
        'heading':"i am isha kule"
        'content':"u am from seit"
    }
    return HttpResponse("hey isha")
