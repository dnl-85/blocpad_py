#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os, sys, getpass
from datetime import date, datetime

####################################################################################################
### blocpad.py  -  bloc-note en mode CLI et discussion sur LAN
### mai 2022 - sous License MIT - par MEYER Daniel pour Linux, Mac et Windows.
####################################################################################################
### contact : meyer.daniel67@protonmail.com OU https://t.me/dnl_85
### dépôt   : https://github.com/dnl-85/blocpad_py
####################################################################################################

# fonction principale appelée au lancement du script
# lors de l'appel depuis un CLI, il faudra spécifié le mode et le fichier à lire, à surveiller ou
# à modifier
def main(option):
    datas = option[2]
    if "-r" in option: lire(datas)
    elif "-w" in option: ajout(datas)
    elif "-s" in option: surveille(datas)
    elif "-d" in option: discussion(datas)
    else: print ("... option(s) inconnue(s)...")
    exit()

# fonction permettant la lecture du fichier spécifié en option
# par exemple : python3 blocpad.py -r note.txt
# va lancer le script en mode lecture et lire le fichier note.txt
def lire(datas):
    try:
        with open(datas, "r") as fichier:
            contenu = fichier.read()
        print (f"\n{contenu}\n")
        exit()
    except:
        print("le fichier spécifié n'existe pas !")

# fonction permettant l'écriture d'une note dans le fichier spécifié en option
# par exemple : python3 blocpad.py -w note.txt
# va lancer le script en mode ajout et enregistrer la note saisie dans le fichier spécifié
def ajout(datas):
    message = input(" > ")
    if message != "":
        message = f"{horodatage()}  : {message} \n"
        with open(datas, "a") as fichier:
            fichier.write(message)
        exit()
    else:
        exit()

# fonction permettant la lecture à interval régulier du fichier spécifié en option
# par exemple : python3 blocpad.py -s note.txt
# va lancer le script en mode surveillance et relire le fichier note.txt toutes les 20 secondes
# à noter que ce mode ne lit que les 10 dernières lignes du fichier spécifié
def surveille(datas):
    while True:
        try:
            os.system("clear")
            try:
                with open(datas, "r") as fichier:
                    try:
                        contenu = fichier.readlines()[-10:]
                        for x in contenu:
                            print(x.replace("\n", ""))
                    except:
                        contenu = fichier.read()
                        print(f"\n{contenu}")
                    finally:
                        print(f"\n... EN ATTENTE ... dernier accès : {horodatage()}")
                        print(f"... Ctrl-Z pour terminer et revenir au Terminal ...")
                os.system("sleep 20")
                surveille(datas)
            except:
                print("le fichier spécifié n'existe pas !")
                break
        except KeyboardInterrupt:
            print("... FIN DE L'ECHANGE ...")

# fonction permettant l'écriture dans le fichier spécifié en option, sans sortir du programme
# par exemple : python3 blocpad.py -d note.txt
# va lancer le script en mode discussion et permet de rajouter du contenu au fichier tant que
# l'invite de saisie (input) n'est pas vide. si l'invite est vide, le script s'arrête
def discussion(datas):
    os.system("clear")
    print("...                        EN MODE DISCUSSION                        ...")
    print("... laisser le champs de saisie libre et appuyer sur Entrée pour finir !")
    message = input(" > ")
    if message != "":
        message = f"{horodatage()}  : {message} \n"
        with open(datas, "a") as fichier:
            fichier.write(message)
        discussion(datas)
    else:
        exit()

# fonction permettant simplement de concaténer une ligne regroupant le nom de l'utilisateur du pc
# utilisé, le jour et l'heure
def horodatage():
    jour = date.today()
    heure = datetime.now()
    login = getpass.getuser()
    moment = login + " - " + jour.strftime("%d/%m/%Y") + " - " + heure.strftime("%H:%M:%S")
    return moment

####################################################################################################
### lancement du programme...
####################################################################################################"
main(sys.argv)
