from django.shortcuts import render

links_dict = {"main": "index.html", "login": "logging_page.html"}


# Create your views here.
def main_page(request):
    """
    Logging page (via VK)

    """
    return render(request, "index.html")


def show_page(request, page_name: str):
    link = links_dict.get(page_name)
    if link:
        return render(request, "{0}".format(link))
    else:
        # return HttpResponseNotFound(f"Такой страницы не существует - {page_name}")
        return render(request, "not_found_page.html")
