# Ce module est le module principal qu’on lance au niveau de l’éditeur de commande pour chaque noeud
# il represente l'architecture du noeud peer to peer (client/serveur)
# dans ce module on determine le port du noeud et s'il possede le token au depart
# on initialise l'election (au debut chaque noeud se considere comme leader)
# et on fait appel au autres modules pour la partie client et serveur

#importer les modules 
from Lib import *
from component_node.Part_In import *
from component_node.Part_Out import *
from component_node.elect import *

PORT_In=int(sys.argv[1]) # Récupérer le numéro de port entré par l'utilisateur
Have_Token=int(sys.argv[2]) #1: possède le token , 0: sinon

Sd_Out=Part_Out() #Lancer un thread pour Part_Out --> partie qui gère le socket client

# initialisation de l'election
elect = election(PORT_In,Sd_Out)

#Lancer et activer un thread pour Part_In --> partie qui gère le socket serveur
Sd_In=Part_In(PORT_In,Have_Token,Sd_Out,elect)
Sd_In.start()

#activer le thread Sd_Out
Sd_Out.port_next_Neighbor=int(input("Numéro de port du voisin: "))
Sd_Out.start()

