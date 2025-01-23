from flask import Flask,request, jsonify
from flask_cors import CORS
import os
import smtplib
import smtplib
import email.message
import jwt
import json
from datetime import date, timedelta, datetime
import hashlib
import random

from User import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

#constantes
secretKey = '711641683'

@app.route('/cad', methods=['POST'])
def cadastro ():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    consumer = request.json.get('consumer')
    delivery = request.json.get('delivery')
    store = request.json.get('store')
    driverLicence = request.json.get('driverLicence')
    birth = request.json.get('birth')
    userId = request.json.get('userId')
    storeRegister = request.json.get('storeRegister')

    print(name, email, password, consumer, delivery, store, driverLicence, birth, userId, storeRegister)

    # verificando se o cadastro já existe
    user = User(email)
    check = user.checkUser()
    print(check)
    if check:
        return jsonify({"status": "usuário já cadastrado"})
    else:
        # cadastrando usuário
        # user.add_user()
        # id = user.checkUser()[0]
        # config = Config(user.checkUser()[0])
        # config.criarCampos()

        # gerar token para verificação de email
        # gerar code
        code = random.randint(1000, 100000)
        print(code)

        # enviar email
        corpo_email = f"<p>Olá, esse é seu código de verificação é <b>{code}</b>, ele vai expirar em 5 minutos</p>"

        msg = email.message.Message()
        print(msg)
        msg['Subject'] = "Código Adapt.AI"
        msg['From'] = 'adapt.AiEducation@gmail.com'
        msg['To'] = f'{email}'
        password = 'yxfi sovv kztw tgml'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # entrando com as credenciais
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

        global secretKey
        payload = {'code': code, 'nome': name, 'email': email, 'senha': password}
        token = jwt.encode(payload, secretKey, algorithm='HS256')

        # calculo de vencimento
        to_day = datetime.now()
        td = timedelta(minutes=5)

        print(to_day + td)

        print({'status': True, 'resp': {'key': token, 'down': to_day + td}})
        return jsonify({'status': True, 'resp': {'key': token, 'down': to_day + td}})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
