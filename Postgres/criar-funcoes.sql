create or replace function SelectRestaurantes() RETURNS TABLE (
    id integer,
    nome VARCHAR(20),
    email VARCHAR(50),
    telefone VARCHAR(9),
    morada VARCHAR(50)
) 
LANGUAGE plpgsql
as $body$
begin
	return query select restaurantes.id_restaurante,restaurantes.nome,restaurantes.email,restaurantes.telefone,restaurantes.morada from restaurantes;
end;
$body$;

create or replace function SelectRestaurante(id_r integer) RETURNS TABLE (
    id integer,
    nome VARCHAR(20),
    email VARCHAR(50),
    telefone VARCHAR(9),
    morada VARCHAR(50)
) 
LANGUAGE plpgsql
as $body$
begin
	return query select restaurantes.id_restaurante,restaurantes.nome,restaurantes.email,restaurantes.telefone,restaurantes.morada from restaurantes where restaurantes.id_restaurante=id_r;
end;
$body$;

create or replace function SelectEmentasRestaurante(id_r integer) RETURNS TABLE (
    id integer,
    designacao_ementa VARCHAR(15),
    preco money,
    designacao_tipo VARCHAR(15),
    designacao_refeicao VARCHAR(15)
) 
LANGUAGE plpgsql
as $body$
begin
	return query select ementas.id_ementa,ementas.designacao,ementas.preco,tipo_ementas.designacao,tipo_refeicoes.designacao
										from ementas join tipo_ementas
											on ementas.id_tipo_ementa=tipo_ementas.id_tipo_ementa join tipo_refeicoes
												on ementas.id_tipo_refeicao=tipo_refeicoes.id_tipo_refeicao join datas
													on ementas.id_data=datas.id_data
										where ementas.id_restaurante=id_r;
end;
$body$;

create or replace function InsertRestaurante(nome varchar(20),email varchar(50),telefone varchar(9),morada varchar(50)) returns boolean 
LANGUAGE plpgsql
as $body$
begin
	insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT,nome,email,telefone,morada);
	return 1;
end;
$body$;

create or replace function SearchRestaurante(str varchar(20)) RETURNS TABLE (
    id integer,
    nome VARCHAR(20),
    email VARCHAR(50),
    telefone VARCHAR(9),
    morada VARCHAR(50)
) 
LANGUAGE plpgsql
as $body$
begin
	return query select restaurantes.id_restaurante,restaurantes.nome,restaurantes.email,restaurantes.telefone,restaurantes.morada 
	from restaurantes 
	where restaurantes.nome like '%' || str || '%';
end;
$body$;

create or replace function SelectItens() RETURNS TABLE (
    id integer,
    designacao VARCHAR(50)
) 
LANGUAGE plpgsql
as $body$
begin
	return query select * from itens;
end;
$body$;


