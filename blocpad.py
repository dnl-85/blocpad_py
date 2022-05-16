#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os, sys
from datetime import datetime

os.system("clear")
print(f" > BLOCPAD_PY <")

if "-r" in sys.argv:
    with open("blocpad.txt", "r") as fichier:
        contenu = fichier.read()
    print (f"\n{contenu}\n")
elif "-w" in sys.argv:
    message = input(" > ")
    message = f"{str(datetime.now())}  : {message} \n"
    with open("blocpad.txt", "a") as fichier:
        fichier.write(message)
else:
    print ("... option(s) inconnue(s)...")
    
