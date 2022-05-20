# blocpad_py
### un bloc-note en mode CLI sous Python3
-----
un petit script d'exemple permettant de lire et d'écrire dans un fichier texte avec Python3, en utilisant des arguments lors de l'appel du script depuis un terminal.  
pour écrire dans le fichier texte, il suffit de taper la commande suivante :  

    python3 blocpad.py -w fichier_texte.txt

pour lire le fichier texte, il suffit de taper la commande suivante :  

    python3 blocpad.py -r fichier_texte.txt
    
pour surveiller un fichier texte, il suffit de taper la commande suivante :  

    python3 blocpad.py -s fichier_texte.txt
    
pour discuter dans un fichier texte avec d'autres utilisateurs connectés au même fichier texte, il suffit de taper la commande suivante :  

    python3 blocpad.py -d fichier_texte.txt
    
vous aurez compris ici que *ficier_texte.txt* peut être remplacé par le fichier de votre choix.  
pour le reste, vous pouvez vous éclater à le mettre à votre sauce ;)  

-----

le script shell 'blocpad' est un script taillé pour bash / Linux. ce dernier permet de s'économiser l'écriture en entier des 4 commandes ci-dessus... il prend en paramètre 2 arguments (le mode d'utilisation du script et le nom du fichier texte sur lequel opérer), de ce fait, la syntaxe devient alors très simple pour utiliser le programme :  
pour écrire dans un fichier texte, il suffit de taper la commande suivante :

    ./blocpad -w fichier_texte.txt

pour lire le fichier texte, il suffit de taper la commande suivante :

    ./blocpad -r fichier_texte.txt

pour surveiller un fichier texte, il suffit de taper la commande suivante :  

    ./blocpad -s fichier_texte.txt
    
pour discuter dans un fichier texte avec d'autres utilisateurs connectés au même fichier texte, il suffit de taper la commande suivante :  

    ./blocpad -d fichier_texte.txt
    
-----

concernant le script, j'ai mis plus d'infos en commentaires dans le script lui même. jetez y un oeil pour en savoir plus...
la fréquence de rafraichissement en mode surveillance est de 20 secondes. ce délai peut bien sûr être modifié.  
pour l'utilisation en mode surveillance / discussion, j'utilise personnellement le terminal *konsole* (la version du terminal $bash sous KDE), simplement car c'est le seul que je connaisse qui permet de scinder la fenêtre du terminal en 2, voir plus, dans le sens gauche-droite ou haut-bas... d'un coté je lance le script en mode surveillance, de l'autre en mode discussion... et ça fait presque comme un tchat bien old-school :D .
    
Daniel, le 16 / 05 / 2022.
