from django.contrib import admin

from listings.models import Band, Song
class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs
# que nous voulons sur l'affichage de la liste
class SongAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'duration', 'band') # liste les champs
# que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin)

admin.site.register(Song, SongAdmin)