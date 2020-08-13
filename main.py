from flask import Flask, jsonify, request
import json

app = Flask(__name__)

devs = [
    {
        'id':1,
        'responsável':'Lucas',
        'tarefa':'Desenvolver método GET',
        'status':'Concluído'
    },
    {
        'id':1,
        'responsável':'Toledo',
        'tarefa':'Desenvolver método POST',
        'status':'Em andamento'
    },
    {
        'id':2,
        'responsável':'Fernandes',
        'tarefa':'Desenvolver método DELETE',
        'status':'Em andamento'
    }

#Devolve  um desenvolvedor por ID, tbm altera e deleta um dev
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído'})

#Lista todos devs e permite registrar um novo dev
@app.route('/dev/', methods=['POST','GET'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return jsonify(devs[posicao])
    elif request.method == 'GET':
        return jsonify(devs)

if __name__ == '__main__':
    app.run(debug=True)