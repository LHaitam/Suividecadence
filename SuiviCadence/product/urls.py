from django.urls import path
from . import views

urlpatterns = [

    path('lignes_production/', views.liste_lignes_production, name='liste_lignes_production'),  # URL pour afficher la liste des lignes de production
    path('lignes_production/<int:ligne_production_id>/', views.details_ligne_production, name='details_ligne_production'),  # URL pour afficher les détails d'une ligne de production spécifique
    path('lignes_production/ajouter/', views.ajouter_ligne_production, name='ajouter_ligne_production'),  # URL pour ajouter une nouvelle ligne de production
    path('lignes_production/modifier/<int:pk>/', views.modifier_ligne_production, name='modifier_ligne_production'),
    path('lignes_production/supprimer/<int:pk>/', views.supprimer_ligne_production, name='supprimer_ligne_production'),
    path('produits/', views.liste_produits, name='liste_produits'),  # URL pour afficher la liste des produits
    path('produit/<int:produit_id>/', views.produit, name='produit'),
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),  # URL pour ajouter un nouveau produit
    path('produits/modifier/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),  # URL pour modifier un produit
    path('produits/supprimer/<int:pk>/', views.supprimer_produit, name='supprimer_produit'),  # URL pour supprimer un produit
    path('produits/details/<int:pk>/', views.produit, name='details_produit'),  # URL pour afficher les détails d'un produit spécifique
    path('objectifs_hebdo/ajouter/', views.ajouter_objectif_hebdo, name='ajouter_objectif_hebdo'),  # URL pour ajouter un nouvel objectif hebdomadaire
    path('objectifs_hebdo/modifier/<int:pk>/', views.modifier_objectif_hebdo, name='modifier_objectif_hebdo'),  # URL pour modifier un objectif hebdomadaire
    path('objectifs_hebdo/supprimer/<int:pk>/', views.supprimer_objectif_hebdo, name='supprimer_objectif_hebdo'),  # URL pour supprimer un objectif hebdomadaire
]
