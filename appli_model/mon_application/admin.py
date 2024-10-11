from django.contrib import admin
# Register your models here.

from .models import ExempleModel

class ExempleModelAdmin(admin.ModelAdmin):
    # Liste des champs à afficher dans l'interface d'administration
    list_display = ('id', 'nom', 'quantité', 'date_publication', 'prix')  # Remplacez par vos champs réels

    # Recherche par certains champs
    search_fields = ('nom', 'date_publication', 'prix')  # Ajoutez les champs pour la recherche

# Enregistrement du modèle avec la classe personnalisée
admin.site.register(ExempleModel, ExempleModelAdmin)