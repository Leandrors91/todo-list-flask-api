from flask import jsonify,make_response,Flask,request
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="MyUser",
    password="MainPassword",
    database="PYCODERBR",
)

atividades = ['preparar','mirar','atirar']

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/atividades',methods=['GET'])
def get_atividade():
    my_cursor = mydb.cursor()
    my_cursor.execute('select * from atividades')
    my_atividades = my_cursor.fetchall()
    atividades = list()
    for atividade in my_atividades:
        atividades.append(
            {
                'id':atividade[0],
                'nome':atividade[1],
                'descricao':atividade[2],
                'realizado':atividade[3],
                'prioridade':atividade[4]
            }
        )
        
    return make_response(jsonify(
        mensagem='Lista de atividades',
        atividades=atividades
    ))

@app.route('/atividades',methods=['POST'])
def post_atividade():
    atividade = request.json
    my_cursor = mydb.cursor()
    sql = f'insert into atividades (nome,descricao,realizado,prioridade) values ("{atividade["nome"]}","{atividade["descricao"]}","{atividade["realizado"]}","{atividade["prioridade"]}")'
    my_cursor.execute(sql)
    mydb.commit()
    return make_response(jsonify(
        mensagem='Atividade adicionada com sucesso',
        atividades=atividade
    ))
    
@app.route('/atividades',methods=['DELETE'])
def delete_atividade():
    atividade = request.json
    my_cursor = mydb.cursor()
    sql = f'delete from atividades where id = {atividade["id"]}'
    my_cursor.execute(sql)
    mydb.commit()
    return make_response(jsonify(
        mensagem='Atividade deletada com sucesso',
        atividades=atividade
    ))
    
@app.route('/atividades',methods=['PUT'])
def put_atividade():
    atividade = request.json
    my_cursor = mydb.cursor()
    sql = f"UPDATE atividades SET nome='{atividade['nome']}', descricao='{atividade['descricao']}', realizado='{atividade['realizado']}', prioridade='{atividade['prioridade']}' WHERE id = {atividade['id']}"
    my_cursor.execute(sql)
    mydb.commit()
    return make_response(jsonify(
        mensagem='Atividade atualizada com sucesso',
        atividades=atividade
    ))
    
@app.route('/atividades',methods=['PATCH'])
def patch_atividade():
    atividade = request.json
    my_cursor = mydb.cursor()
    sql = f"UPDATE atividades SET realizado='{atividade['realizado']}' WHERE id = {atividade['id']}"
    my_cursor.execute(sql)
    mydb.commit()
    return make_response(jsonify(
        mensagem='Atividade atualizada com sucesso',
        atividades=atividade
    ))

app.run(debug=True)