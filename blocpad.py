#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os, sys, getpass
from datetime import date, datetime

def main(option):
    if "-r" in option: lire()
    elif "-w" in option: ajout()
    else: print ("... option(s) inconnue(s)...")
    exit()

def lire():
    with open("blocpad.txt", "r") as fichier:
        contenu = fichier.read()
    print (f"\n{contenu}\n")
    exit()

def ajout():
    message = input(" > ")
    message = f"{horodatage()}  : {message} \n"
    with open("blocpad.txt", "a") as fichier:
        fichier.write(message)
    exit()
       
def horodatage():
    jour = date.today()
    heure = datetime.now()
    login = getpass.getuser()
    moment = login + " - " + jour.strftime("%d/%m/%Y") + " - " + heure.strftime("%H:%M:%S")
    return moment

main(sys.argv)
