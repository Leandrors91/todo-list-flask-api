# inicia data base
db = [{
    'id':1,
    'nome':'Pular corda',
    'descricao':'30 minutos',
    'realizado':False,
    'prioridade':'Alta'
}]

# insert
def insert(id,nome,descricao,realizado,prioridade):
    atividade = {
    'id': id,
    'nome': nome,
    'descricao': descricao,
    'realizado': realizado,
    'prioridade': prioridade
}
    db.append(atividade)
    print('atividade inserida com sucesso')

# update
def update(id,nome,descricao,realizado,prioridade):
    for atividade in db:
        if atividade['id']==id:
            atividade |= {
                'id':id,
                'nome': nome,
                'descricao': descricao,
                'realizado': realizado,
                'prioridade': prioridade
            }
            break
    print('atividade atualizada com sucesso')

# delete
def delete(id):
    for atividade in db:
        if atividade['id']==2:
            db.remove(atividade)
            break
    print('atividade deletada com sucesso')

# select id
def select(id):
    item = None
    for atividade in db:
        if atividade['id']==id:
            item = atividade
    print(atividade)

# list all
def select_all():
    print(db)

select_all()
insert(2,'Tomar whey','Pos treino',False,'Alta')
select(2)
update(2,'Tomar creatina','Pos treino',False,'Alta')
select(2)
delete(2)
select_all()