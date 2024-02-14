from django.shortcuts import render

# Create your views here.
def dies(request):
    return render(request, "dies.html")
