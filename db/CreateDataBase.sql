use MyDb;

create table atividades(
    id int not null auto_increment,
    nome varchar(100),
    descricao varchar(255),
    realizado varchar(10),
    prioridade varchar(100),
    primary key(id)
);

set character_set_client = utf8;
set character_set_connection = utf8;
set character_set_results = utf8;
set collation_connection = utf8_general_ci;

insert into atividades (nome,descricao,realizado,prioridade) values ('Pular corda','30 minutos','Sim','Alta');