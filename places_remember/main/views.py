from django.shortcuts import render

# Create your views here.


def auth_vk(request):
    return render(request, "index.html")
