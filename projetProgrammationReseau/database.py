import mysql.connector
from mysql.connector import Error

#Fonction qui verifie si l'adresse mail saisie est dans la base de donnée 
def VerifierMail(liste) -> list:
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='USER',
                                            user='root',
                                            password='root')

        sql_select_Query = f"select * from user where mail = '{liste[1]}'"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        return cursor.rowcount == 0

    except mysql.connector.Error as e:
        return False

#Fonction qui enregistre le client dans la base de donnée
def Inscription(list) -> list:
    if VerifierMail(list) == False:
        return False

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='USER',
                                            user='root',
                                            password='root')

        mySql_insert_query = f"""INSERT INTO user(nom, mail, password) 
                            VALUES 
                            ('{list[0]}', '{list[1]}', '{list[2]}') """

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        cursor.close()
        return True

    except mysql.connector.Error as error:
        return False

#Fonction qui permet de connecter un client existant dans la base de donnée
def Connexion(liste)-> list:
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='USER',
                                            user='root',
                                            password='root')

        sql_select_Query = f"select * from user where mail = '{liste[0]}' AND password = '{liste[1]}'"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        return cursor.rowcount == 1

    except mysql.connector.Error as e:
        return False
