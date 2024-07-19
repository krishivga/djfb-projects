from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page_view(request):  # Creating a function to render homepage view
    # Should print hello world onto the webpage
    return HttpResponse("Hello, World!")
