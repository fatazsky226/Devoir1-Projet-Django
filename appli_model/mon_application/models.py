from django.db import models

class ExempleModel(models.Model):
    nom = models.CharField(max_length=100)  # Champ de texte
    description = models.TextField()  # Champ de texte long
    quantité = models.IntegerField()  # Champ d'entier
    prix = models.DecimalField(max_digits=10, decimal_places=2)  # Champ décimal
    date_publication = models.DateField()  # Champ de date
    date_heure_creation = models.DateTimeField(auto_now_add=True)  # DateTime automatique
    est_disponible = models.BooleanField(default=True)  # Champ booléen
    fichier = models.FileField(upload_to='fichiers/')  # Champ fichier
    image = models.ImageField(upload_to='images/')  # Champ image
    email = models.EmailField()  # Champ email

    def __str__(self):
        return self.nom

