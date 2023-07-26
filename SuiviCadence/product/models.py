from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


##########################################################################################################################################################
# Modèle LigneProd pour représenter les lignes de production de l'usine

    
class LigneProd(models.Model):
    nom = models.CharField(max_length=100)
    etat = models.CharField(max_length=2, choices=[('OK', 'OK'), ('KO', 'KO')])  # L'état de la ligne de production (OK ou KO)
    commentaire = models.CharField(max_length=300, null=True,)  # Un commentaire sur l'état de la ligne de production

    def save(self, *args, **kwargs):
        # Vérifier si la ligne de production existe déjà en base de données
        is_new_line = self.pk is None

        # Appeler la méthode save() d'origine pour sauvegarder la ligne de production
        super().save(*args, **kwargs)

        # Enregistrer l'état de la ligne dans la table EtatLigne
        if is_new_line:
            # Si c'est une nouvelle ligne de production, créer un nouvel état avec l'état initial "OK" et le commentaire "Création de la ligne"
            EtatLigne.objects.create(ligne_production=self, etat='OK', commentaire='Création de la ligne')
        else:
            # Si la ligne de production existe déjà, créer un nouvel état avec l'état modifié et le commentaire "Modification de l'état"
            EtatLigne.objects.create(ligne_production=self, etat=self.etat, commentaire='Modification de l\'état')
    
    def __str__(self):
        return f"{self.nom} - État : {self.etat} - Commentaire : {self.commentaire}"
    

##########################################################################################################################################################
# Modèle Produit pour représenter les produits fabriqués dans l'usine


def upload_to(instance, filename):
    return f'images/produits/{filename}'

class Produit(models.Model):
    reference = models.CharField(max_length=100)  # La référence du produit
    nom = models.CharField(max_length=200)  # Le nom du produit
    photo = models.ImageField(upload_to=upload_to, null=True, blank=True)  # La photo du produit (optionnelle)
    ligne_production = models.ForeignKey(LigneProd, on_delete=models.CASCADE, related_name='produits')  # La ligne de production à laquelle le produit est associé

    def __str__(self):
        return f"{self.nom} - Référence : {self.reference} - Ligne : {self.ligne_production.nom}"


##########################################################################################################################################################
# Modèle ObjectifHebdo pour représenter les objectifs hebdomadaires de production

class ObjectifHebdo(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    numero_semaine = models.IntegerField(default=1)  # Ajouter une valeur par défaut ici
    choix_clients = (
        ("Airbus", "Airbus"),
        ("Boeing", "Boeing"),
        ("Comac", "Comac"),
    )
    client = models.CharField(choices=choix_clients, max_length=30)
    date_debut = models.DateField()
    date_fin = models.DateField()
    quantite = models.IntegerField()
    utilisateur = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.produit.nom} - Client : {self.client}"


##########################################################################################################################################################    
# Modèle Realisation pour représenter les réalisations de production

class Realisation(models.Model):
    objectif_hebdo = models.ForeignKey(ObjectifHebdo, on_delete=models.CASCADE)  # L'objectif hebdomadaire auquel la réalisation est associée
    quantite = models.IntegerField()  # La quantité produite pour cette réalisation
    date_heure = models.DateTimeField(auto_now_add=True)  # La date et l'heure de la réalisation
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)  # L'utilisateur qui a enregistré la réalisation

    def __str__(self):
        return f"Réalisation de {self.objectif_hebdo.produit.nom} - Quantité : {self.quantite} - Date : {self.date_heure}"


##########################################################################################################################################################
# Modèle MouvementTempsReel pour représenter les mouvements de production en temps réel

class MouvementTempsReel(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)  # Le produit associé au mouvement
    date_heure = models.DateTimeField(auto_now_add=True)  # La date et l'heure du mouvement
    quantite = models.IntegerField()  # La quantité ajoutée ou soustraite dans le mouvement
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)  # L'utilisateur qui a enregistré le mouvement
    soustraction = models.BooleanField(default=False)  # Un drapeau pour indiquer si la quantité est soustraite (True) ou ajoutée (False)

    def __str__(self):
        mouvement_type = "Soustraction" if self.soustraction else "Addition"
        return f"{mouvement_type} de {self.quantite} unité(s) - Produit : {self.produit.nom} - Date : {self.date_heure}"


##########################################################################################################################################################
# Modèle EtatLigne pour représenter les états des lignes de production

class EtatLigne(models.Model):
    ligne_production = models.ForeignKey(LigneProd, on_delete=models.CASCADE)  # La ligne de production associée à l'état
    commentaire = models.CharField(max_length=300)  # Un commentaire sur l'état de la ligne de production
    date_heure = models.DateTimeField(auto_now_add=True)  # La date et l'heure de l'enregistrement de l'état
    utilisateur = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    CHOICES_ETAT = (
        ('OK', 'OK'),
        ('KO', 'KO'),
    )
    etat = models.CharField(max_length=2, choices=CHOICES_ETAT, default='OK')

    def __str__(self):
        formatted_date = self.date_heure.strftime('%d/%m/%y %H:%M:%S')
        return f"État de {self.ligne_production.nom} - État : {self.etat} - Commentaire : {self.commentaire} - Date et heure : {formatted_date}"


