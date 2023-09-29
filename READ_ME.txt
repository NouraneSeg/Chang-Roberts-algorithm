--------------------------------------------------
On a ajouté une capture d'écran de l'execution dans le dossier principal
Chaque module et chaque etape sont expliqués en commentaires
------------------------------------------------------------------------------------------------------------

dans ce projet on a implémenté l’algorithme d’élection de Chang et Roberts.

pour l'executer veillez ouvrir 03 terminaux, lancer Node.py dans chaque terminal


1. Donner les numeros de ports suivis par 0/1 ( un seul initiateur = 1 )
exemple:
>python Node.py 1001 1
>python Node.py 1002 0
>python Node.py 1003 0

2. Établir la connexion en donnant le Numéro de port distance.
exemple:
>python Node.py 1001 1
Numéro de port du voisin: 1002
>python Node.py 1002 0
Numéro de port du voisin: 1003
>python Node.py 1003 0
Numéro de port du voisin: 1001

3. Taper entrer pour commencer l'élection
