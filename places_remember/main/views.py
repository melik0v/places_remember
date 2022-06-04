from django.shortcuts import render
from django.http import HttpResponseNotFound


links_dict = {"main": "index.html", "": "index.html"}


# Create your views here.
def main_page(request):
    return render(request, "index.html")


def show_page(request, page_name: str):
    link = links_dict.get(page_name)
    if link:
        return render(request, "{0}".format(link))
    else:
        return HttpResponseNotFound(f"Такой страницы не существует - {page_name}")
