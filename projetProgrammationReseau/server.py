import socket
import time
import json
import database

#Fonction qui permet au serveur de recupérer les informations d'inscription d'un client
def Inscription(client:socket, buffer:int):
    liste = list()
    req = "Veuillez enter votre nom complet: " 
    client.send(req.encode("utf-8")) 
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Veuillez entrer votre adresse mail:"
    client.send(req.encode("utf-8")) 
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    requete1 = "mdp1"
    requete2 = "mdp2"

    while requete1 != requete2:
        req = "Veuillez entrer votre mot de passe :"
        client.send(req.encode("utf-8"))
        requete1 = client.recv(buffer)

        req = "Veuillez confirmer votre mot de passe :"
        client.send(req.encode("utf-8")) 
        requete2 = client.recv(buffer)

        if requete1 != requete2:
            req = "Les mots de passe ne sont pas identiques"
            client.send(req.encode("utf-8"))
        else:
            req = "Les mots de passe sont identiques"
            client.send(req.encode("utf-8"))

    liste.append(requete1.decode("utf-8"))
    if database.Inscription(liste) == True:
        req = "Inscription reussie"
        client.send(req.encode("utf-8"))
    else:
        req = "Echec de lors de l'inscription"
        client.send(req.encode("utf-8")) 

#Fonction qui permet au serveur de recupérer les informations de connexion d'un client
def Connexion(client:socket,buffer:int):
    liste = list()
    req = "Veuillez entrer votre adresse mail svp :"
    client.send(req.encode("utf-8")) 
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Veuillez entrer votre mot de passe svp :"
    client.send(req.encode("utf-8")) 
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    if database.Connexion(liste) == True:
        req = "Connexion reussie "
        client.send(req.encode("utf-8")) 
    else:
        req = "Echec de lors de la connexion !!!"
        client.send(req.encode("utf-8")) 

#Fonction qui permet de se conecter au serveur
def ouvrirServeur(host,
               port,
               buffer=1024):
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((host,port))
    serveur.listen(5)

    client, infosClient = serveur.accept()
    print("Vous etes connecté. Adresse " + infosClient[0])  

    while True:    
        
        reponse = "Tapez 1 si vous voulez vous inscrire Tapez 2 si vous voulez vous connecter et Tapez 3 si vous voulez quitter"
        client.send(reponse.encode("utf-8"))
        time.sleep(2)

        requete = client.recv(buffer)
        requete_decode = requete.decode("utf-8")

        if requete_decode == "1":
            Inscription(client,buffer)

        elif requete_decode == "2":
            Connexion(client,buffer)

        elif requete_decode == "3":         
            req = "Au revoir !!!"
            client.send(req.encode("utf-8")) 
            client.close()
            break

    serveur.close()
           
    


if __name__ == "__main__":
    
    ouvrirServeur('192.168.10.1', 50000)
