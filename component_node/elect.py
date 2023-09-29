# Ce module contient l'algorithme de l'election
# on commence par associer a chaque noeud un id aleatoire
# au debut chaque noeud se considere comme leader
# on a pour but de passer le message dans le token ring
# jusqu'a avoir determiné le noeud avec le plus grand id --> le leader
# on arrete quand chaque noeud a recu la même valeur Leader_ID et Leader_Port 2 fois

from Lib import *

class message():

    def __init__(self, id_elect, port_elect):
        self.type= "ELECT"
        self.id_elect= id_elect
        self.port_elect= port_elect

class election():

    #initialisation de l'election
    def __init__(self,port,Sd_Out):
        self.etat="en cours"
        ID=random.randint(1,100)
        print("ID = ",ID)
        self.Leader_ID=ID
        self.Leader_Port=port
        self.Sd_Out = Sd_Out

    def run(self,MSG):
        print("------------------------------------------------")
        print("Le message reçu : id=",MSG.id_elect," port=",MSG.port_elect)

        # verfier si ce noeud reçoie ce message pour la deuxieme fois (meme id et port)
        if MSG.id_elect==self.Leader_ID and MSG.port_elect==self.Leader_Port:
            # ne plus faire l'election pour ce noeud
            print("election terminée")
            self.etat="terminée"
            print("Je sais que le leader est le noeud numero : ",self.Leader_ID," avec le port : ",self.Leader_Port)

        # comparer les ids et mettre l'id du msg comme nouveau leader s'il est superieur
        elif MSG.id_elect>self.Leader_ID:
            print("Leader_ID=",self.Leader_ID," < msg.id_elect=",MSG.id_elect)
            self.Leader_ID=MSG.id_elect
            self.Leader_Port=MSG.port_elect
        else : # sinon on mets l'id de ce noeud dans le message s'il est superieur
            print("Leader_ID=",self.Leader_ID," > msg.id_elect=",MSG.id_elect)
            MSG.id_elect=self.Leader_ID
            MSG.port_elect=self.Leader_Port

        # envoyer le message modifié au noeud suivant
        self.Sd_Out.s.send(str(MSG.id_elect).encode())
        self.Sd_Out.s.send(str(MSG.port_elect).encode())
        print("message modifié envoyé au noeud suivant")
        self.Sd_Out.resume() #liberer le token