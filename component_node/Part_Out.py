# Ce module represente la partie client du noeud
# on cree un socket client et on le connecte avec le noeud suivant
# on bloque ensuite l'envoie du token et le libere apres lenvoie du message "TOKEN" dans part in

from Lib import *

class Part_Out(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
        self.port_next_Neighbor=0 #Initiatialiser le port du noeud voisin
        
        #créer socket appelée s (self.s)
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__flag = threading.Event() #Créer un objet event
        self.__flag.clear() # Set to False
         
    def run (self) :
        try:
            # Se connecter au socket Sd_In du noeud suivant avec le port "self.port_next_ Neighbor"
            self.s.connect(("127.0.0.1",self.port_next_Neighbor))
        except:
            print ("La partie OUT n'arrive pas à se connecter au voisin")
            sys.exit ()

        while True:
            self.__flag.wait() # bloquer le thread
            self.s.send(b"TOKEN") # envoyer le token
            self.__flag.clear()
    
    def resume(self):
        self.__flag.set()