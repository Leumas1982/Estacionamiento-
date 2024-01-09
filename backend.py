# backend.py
from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        if username not in users:
            users[username] = password
            return jsonify({'message': 'Usuario registrado con éxito'})
        else:
            return jsonify({'error': 'El usuario ya existe. Elija otro nombre de usuario.'}), 400
    else:
        return jsonify({'error': 'Ingrese un nombre de usuario y una contraseña válidos.'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        if username in users and users[username] == password:
            return jsonify({'message': 'Inicio de sesión exitoso'})
        else:
            return jsonify({'error': 'Nombre de usuario o contraseña incorrectos.'}), 401
    else:
        return jsonify({'error': 'Ingrese un nombre de usuario y una contraseña válidos.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
