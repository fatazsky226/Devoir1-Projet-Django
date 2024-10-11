from django.urls import path
from . import views

urlpatterns = [

    path('objets/', views.liste_objets, name='liste_objets'),  # Lien vers la vue liste_objets
    path('exemple_model/', views.exemple_model_view, name='exemple_model'),
]
