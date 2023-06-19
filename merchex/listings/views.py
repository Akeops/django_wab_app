from django.shortcuts import render

from listings.models import Band, Titre


def index(request):
    bands = Band.objects.all()
    titres = Titre.objects.all()
    return render(request, "listings/index.html", context={'bands': bands , 'titres': titres})

def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"listings/article_{numero_article}.html")
    return render(request, f"listings/article_not_found.html")
