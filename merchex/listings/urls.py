from django.urls import path
from .views import listeGroupeEtSong, detailGroupe, contact, emailSent, bandCreate, songCreate, updateBand, updateSong

urlpatterns = [
    path('', listeGroupeEtSong, name="liste-groupes"),
    path('<int:id>/', detailGroupe, name="detail-groupe"),
    path('contact-us/', contact, name="contact"),
    path('contact-us/email-sent', emailSent, name="email-sent"),
    path('add/', bandCreate, name='band-create'),
    path('addSong/', songCreate, name='song-create'),
    path('<int:id>/update', updateBand, name='update-band'),
    path('<int:id>/updateSong', updateSong, name='update-song')
]

