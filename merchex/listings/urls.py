from django.urls import path
from .views import listeGroupeEtSong, detailGroupe, contact

urlpatterns = [
    path('', listeGroupeEtSong, name="liste-groupes"),
    path('<int:id>/', detailGroupe, name="detail-groupe"),
    path('contact/', contact, name="listings-contact"),
]

