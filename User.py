from Conection import *
import hashlib

class User:
    def __init__(self,email, password ='', name = '', consumer = False, delivery = False, store = False, driverLicence = 0, birth = 0, userId = 0, storeRegister = 0,autentic = 0):
        self.name = name
        self.password = password
        self.email = email
        self.consumer = consumer
        self.delivery = delivery
        self.store = store,
        self.driverLicence = driverLicence
        self.birth = birth
        self.userId = userId
        self.storeRegister = storeRegister
        self.autentic = autentic

    def checkUser (self):
        query = f'SELECT id FROM `User` WHERE Email = "{self.email}";'
        conexao = Conection()
        exis = conexao.get_query(query)
        return exis