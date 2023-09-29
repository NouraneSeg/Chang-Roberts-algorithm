# Ce module represente la partie serveur du noeud
# ici on cree le socket serveur et on le mets en ecoute passive
# on lance l'election et recoit les messages election en boucle jusqu'a trouver le leader
# Sil ne possède pas le Token on le mets en attente de reception des messages 
# sinon on le donne la parole a c noeud 
# a la fin on passe le token au noeud suivant

from Lib import *
from component_node.elect import *

def Handle_Neighbor(con, add, t, Sortie,elect):
    while True:
        if elect.etat == "en cours":
            MSG = message(0,0) # on initialise une variable de type message election
            if t==0: # si le noeud possede pas le token
                msg=con.recv(1024) # on le mets en attente du message d'election id puis port
                MSG.id_elect = int(msg.decode())
                msg=con.recv(1024)
                MSG.port_elect = int(msg.decode())
                msg=con.recv(1024) # pour recevoir le token
                if msg.decode()=="TOKEN":
                    elect.run(MSG) # lancer l'operation de l'election pour ce noeud
            if t==1:
                input("vous etes l'initiateur du token,tapez entrer pour commencer l'election")
                t=0
                elect.run(MSG) # lancer l'operation de l'election pour le noeud initiateur

        else: # partie reception des message dans else pour la bloquer pendant l'election
            if t==0: # S'il ne possède pas le Token, donc il se met en attente de réception de message.
                msg=con.recv(1024)
                if msg.decode()=="TOKEN": #S'il a reçu le Token l’utilisateur a la main pour saisir un ou plusieurs messages.
                    print("------------------------------------------------")
                    print(" Vous avez reçu le token")
                    print(" Vous avez le droit à la parole")
                    print(" Pour libérer la parole, il faut saisir le mot -- TOKEN--")
                    while True:
                        expression=input("vous pouvez vous exprimer :")
                        if expression=="TOKEN": 
                            break
            if t==1:
                print("vous etes l'initiateur du token,taper entrer pour le liberer")
            t=0
            Sortie.resume() # liberer le token
    
class Part_In (threading.Thread):
    
    def __init__(self, port, T, S,elect):
        threading.Thread.__init__(self)
        
        self.port=port # Initiatialiser le port
        self.T=T # Initiatialiser la valeur de T
        self.Sortie=S # thread Sd_Out
        # creer socket appelee ss (self.ss)
        self.ss=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.elect = elect

        try:
            #attacher le socket declare un une adresse IP «localhost» et numėro de port récupéré dans «self.port»
            self.ss.bind(("127.0.0.1",self.port))
        except:
            print("Le Sd_In n'arrive pas à s'attacher à l'adresse & numéro de port")
            sys.exit()
            
        self.ss.listen() #Mettre socket en mode écoute passivee

    def run(self):
        #Dans la mêthode run(), socket accept une seule demande de connexion
        self.connexion, self.add=self.ss.accept()
        #Appel de la fonction «Handle_Neighbor» qui est définie en haut de ce module Part_In.py
        Handle_Neighbor(self.connexion, self.add, self.T,self.Sortie,self.elect) #changer la valeur de t si linitialeur n'a plus le token