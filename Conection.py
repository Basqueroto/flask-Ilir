import mysql.connector

class Conection:
    def add_query (self, query):
        try:
            conect = mysql.connector.connect(user="root", password="IPSpPLXXeWLJqBoRDpxYJpWGDGIeplcK", host="junction.proxy.rlwy.net", database='railway', port='54210', auth_plugin='mysql_native_password')
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
            conect = mysql.connector.connect(user="root", password="EVAZVDalMqJvPwgpdbwIcQaAnkZePUWE", host="autorack.proxy.rlwy.net", database='railway', port='57960', auth_plugin='mysql_native_password')
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
