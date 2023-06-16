from django.shortcuts import render


def index(request):
    return render(request, "listings/index.html")

def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"listings/article_{numero_article}.html")
    return render(request, f"listings/article_not_found.html")
