#Affichage du générateur de mot de passe
# Author: Kerrian Le Bras

# Affichage dans une fenêtre Tkinter du générateur de mot de passe

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

#Liste des caractères
mini = "abcdefghijklmnopqrstuvwxyz"
maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffre = "0123456789"
symbole = "!@#$%^&*()_+-=[]{};:,./<>?|"

#Fonction de génération du mot de passe
def generer():
    #Récupération des valeurs des variables
    longueur = longueur_var.get()
    nombre = nombre_var.get()
    #Génération du mot de passe, avec un mélange aléatoire des caractères
    mdp = ""
    for i in range(nombre):
        mdp += " "
        for j in range(longueur):
            mdp += random.choice(mini + maj + chiffre + symbole)
    #Affichage du mot de passe
    mdp_label.configure(text=mdp)

#Fonction d'information
def info():
    messagebox.showinfo("Information", "Générateur de mot de passe, par Kerrian Le Bras")

#Fonction d'aide
def aide():
    messagebox.showinfo("Aide", "Entrez la longueur du mot de passe et le nombre de mot de passe à générer")

#Fonction de fermeture
def quitter():
    fenetre.destroy()

#Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Générateur de mot de passe")
fenetre.geometry("400x200")

#Création des variables
longueur_var = tk.IntVar()
nombre_var = tk.IntVar()

#Création des widgets
longueur_label = ttk.Label(fenetre, text="Longueur du mot de passe: ")
longueur_entry = ttk.Entry(fenetre, textvariable=longueur_var)
nombre_label = ttk.Label(fenetre, text="Nombre de mot de passe: ")
nombre_entry = ttk.Entry(fenetre, textvariable=nombre_var)
generer_button = ttk.Button(fenetre, text="Générer", command=generer)
mdp_label = ttk.Label(fenetre, text="")
info_button = ttk.Button(fenetre, text="Information", command=info)
aide_button = ttk.Button(fenetre, text="Aide", command=aide)
quitter_button = ttk.Button(fenetre, text="Quitter", command=quitter)

#Placement des widgets
longueur_label.grid(row=0, column=0, padx=5, pady=5)
longueur_entry.grid(row=0, column=1, padx=5, pady=5)
nombre_label.grid(row=1, column=0, padx=5, pady=5)
nombre_entry.grid(row=1, column=1, padx=5, pady=5)
generer_button.grid(row=2, column=0, padx=5, pady=5)
mdp_label.grid(row=2, column=1, padx=5, pady=5)
info_button.grid(row=3, column=0, padx=5, pady=5)
aide_button.grid(row=3, column=1, padx=5, pady=5)
quitter_button.grid(row=4, column=0, padx=5, pady=5)

#Boucle principale
fenetre.mainloop()

#Fin du programme