from django.shortcuts import render
from listings.models import Band, Song
from listings.forms import ContactUsForm
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

