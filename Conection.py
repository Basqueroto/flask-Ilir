import mysql.connector
import mysql.connector
from mysql.connector import Error

class Conection:
    def add_query (self, query):
        try:
            conect = mysql.connector.connect(
                user="root",
                password="vuXIWSyWOtDLSaeNtlNNQMyXhHgDBYLg",
                host="autorack.proxy.rlwy.net",
                database="railway",
                port=32803
            )
            cursor = conect.cursor()
            inserir = query
            cursor.execute(inserir)
            conect.commit()
            cursor.close()
            conect.close()
            return True

        except mysql.connector.Error as erro:
            print(erro)
            return False

    def get_query(self, query):
        try:
            conect = mysql.connector.connect(
                user="root",
                password="G12A6faE43BA643FgH-Ag5dEF42Gb5dC",
                host="monorail.proxy.rlwy.net",
                database="railway",
                port=48934
            )
            print('conection open')
            cursor = conect.cursor()
            inserir = query
            cursor.execute(inserir)
            di = False
            if cursor:
                exist = True
                for i in cursor:
                    di = i
            else:
                exist = False
            cursor.close()
            conect.close()
            if exist:
                return di
            else:
                return False
        except mysql.connector.Error as erro:
            print(erro)
            return False
