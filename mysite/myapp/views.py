from django.shortcuts import render

# Create your views here.
def index(request):
    data = {"body": "<p> Hello world</p>"}
    return render(request, "home/homepage.html", context=data)