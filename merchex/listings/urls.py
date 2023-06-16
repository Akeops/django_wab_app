from django.urls import path

from .views import index, article

urlpatterns = [
    path('', index, name="listings-index"),
    path('article-<str:numero_article>/', article, name="listings-article")
]