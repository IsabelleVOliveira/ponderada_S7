from flask import Flask, request, render_template, Blueprint, jsonify,redirect
from tinydb import TinyDB, Query
from pydobot import Dobot
from datetime import datetime

app = Flask(__name__)
db = TinyDB('pontos.json')
buscador = Query()


try:
    dobot = Dobot(port="COM7")
    dobot.speed(100)
    dobot_on = True
except:
    print(f"Erro ao conectar com o robô")
    dobot = None

print(dobot)
    
@app.route('/', methods=['GET'])
def start():
    return render_template('index.html')

@app.route('/logs', methods=['GET'])
def logs():
    logs = db.all()
    return render_template('logs.html', logs=db.all())

@app.route('/home', methods=['GET'])
def home():
    if dobot_on:
        dobot.move_to(x=234, y=-30, z=152, r=-7.4)
        db.insert({'Ponto':(234, -30, 152, -7.4), 'command': 'home'})
        return ('', 204)
    else:
        return "nao deu certo"


@app.route('/move', methods=['POST'])
def move():
    if dobot_on:
        command = request.form.get('command')
    # Obter os valores x, y, z e r dos dados da solicitação
        x = float(request.form.get('x'))
        y = float(request.form.get('y'))
        z = float(request.form.get('z'))
        r = float(request.form.get('r'))
        dobot.move_to(x=x, y=y, z=z, r=r)
    # Inserir o ponto no banco de dados
        command = f'x={x}, y={y}, z={z}, r={r})'
        db.insert({'command': command})
    # Retornar uma resposta JSON indicando que o ponto foi inserido com sucesso
        return f'Coodenada inserida com sucesso: <h1>X: {x}, Y: {y}, Z: {z}, R: {r}</h1>'
    else:
        return render_template('index.html') if dobot_on else render_template('logs.html')

@app.route('/changePonto/<int:id>', methods=['PUT'])
def atualizar_ponto(id):
    novo_ponto = request.json  # Recebe o novo ponto do JSON
    db.update(novo_ponto, buscador.id == id)
    return jsonify({'message': 'Ponto atualizado com sucesso'}), 200

@app.route('/deletePonto/<int:id>', methods=['DELETE'])
def deletar():
    with open('pontos.json', 'w') as arquivo:
        arquivo.write('')
    return jsonify({'message': 'Conteúdo do arquivo deletado com sucesso'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

