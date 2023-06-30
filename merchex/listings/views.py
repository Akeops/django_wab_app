from django.shortcuts import render
from listings.models import Band, Song
from listings.forms import ContactUsForm, BandForm, SongForm
from django.core.mail import send_mail
from django.shortcuts import redirect

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
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
        # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
        # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    return render(request,
          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit

def emailSent(request):
    return render(request, 'listings/done.html')

def bandCreate(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('detail-groupe', band.id)

    else:
        form = BandForm()
    return render(request,
            'listings/band_create.html',
            {'form': form})

def songCreate(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()

            return redirect('detail-groupe', song.band.id)

    else:
        form = SongForm()
    return render(request,
            'listings/songCreate.html',
            {'form': form})

def updateBand(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)  # on pré-remplir le formulaire avec un groupe existant

        if form.is_valid():
            form.save()
            return redirect('detail-groupe', band.id)

    else:
        form = BandForm(instance=band)

    return render(request,
                  'listings/updateBand.html',
                  {'form': form})

def updateSong(request, id):
    song = Song.objects.get(id=id)

    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)

        if form.is_valid():
            form.save()
            return redirect('detail-groupe', song.band.id)

    else:
        form = SongForm(instance=song)

    return render(request,
                  'listings/updateSong.html',
                  {'form': form})