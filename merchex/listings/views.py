from django.shortcuts import render
from listings.models import Band, Song

def listeGroupeEtSong(request):
    bands = Band.objects.all()
    songs = Song.objects.all()
    return render(request, "listings/listeBand.html", context={'bands': bands, 'songs': songs})

def detailGroupe(request, id):
    band = Band.objects.get(id=id)
    songs = Song.objects.all()
    return render(request, 'listings/detailGroupe.html', {'band' : band, 'songs': songs})

def listeSong(request):
    songs = Song.objects.all()
    return render(request, 'listings/listeBand.html', context={'songs': songs})

def contact(request):
    return render(request, "listings/contact.html")





