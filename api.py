from flask import Flask, request, jsonify
from models import Cliente, Produto, ServicoBancario
from database import db, init_db

app = Flask(__name__)
init_db(app)

# Rota para criar um cliente
@app.route('/clientes', methods=['POST'])
def criar_cliente():
    dados = request.json
    cliente = Cliente(nome=dados['nome'], email=dados['email'])
    db.session.add(cliente)
    db.session.commit()
    return jsonify({"message": "Cliente criado com sucesso!"}), 201

# Rota para listar clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([{"id": c.id, "nome": c.nome, "email": c.email} for c in clientes])

# Rota para criar um produto
@app.route('/produtos', methods=['POST'])
def criar_produtos():
    dados = request.json  
    if not isinstance(dados, list):
        return jsonify({"message": "Esperado uma lista de produtos"}), 400
    
    for produto_data in dados:
        produto = Produto(nome=produto_data['nome'], preco=produto_data['preco'])
        db.session.add(produto)
    
    db.session.commit()
    return jsonify({"message": f"{len(dados)} produtos criados com sucesso!"}), 201


# Rota para listar produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([{"id": p.id, "nome": p.nome, "preco": p.preco} for p in produtos])

# Rota para criar um serviço bancário
@app.route('/servicos', methods=['POST'])
def criar_servico():
    dados = request.json
    servico = ServicoBancario(descricao=dados['descricao'], taxa=dados['taxa'])
    db.session.add(servico)
    db.session.commit()
    return jsonify({"message": "Serviço bancário criado com sucesso!"}), 201

# Rota para listar serviços bancários
@app.route('/servicos', methods=['GET'])
def listar_servicos():
    servicos = ServicoBancario.query.all()
    return jsonify([{"id": s.id, "descricao": s.descricao, "taxa": s.taxa} for s in servicos])

if __name__ == '__main__':
    app.run(debug=True)
