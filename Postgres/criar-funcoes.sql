----EcraInicial
--Preencher Treeview

create or replace function SelecionarRestaurantes(pesquisa VARCHAR(20) default '',orderby VARCHAR(20) default 'nome',sentido VARCHAR(4)default 'asc' ) RETURNS TABLE (
    id integer,
    nome VARCHAR(20),
    email VARCHAR(50),
    telefone VARCHAR(9),
    morada VARCHAR(50)
) 
LANGUAGE plpgsql
as $body$
begin
	return query execute 'select restaurantes.id_restaurante,restaurantes.nome,restaurantes.email,restaurantes.telefone,restaurantes.morada 
								from restaurantes
								where restaurantes.nome like $$%'|| pesquisa ||
							 '%$$ order by '|| quote_ident(orderby)||' '||sentido;
end;
$body$;

--Exportar XML

create or replace function ExportarXML() returns xml 
LANGUAGE plpgsql
as $body$
DECLARE output XML;
begin
	select xmlelement(name "Restaurantes",xmlagg(xmlelement (name "Restaurantes",
		xmlattributes(id_restaurante as "ID"),
			xmlforest(restaurantes.nome as "nome", restaurantes.email as "email", restaurantes.telefone as "telefone", restaurantes.morada as "morada"), 
				(select xmlagg(xmlelement(name "Ementas",
					xmlforest(designacao as "Designação", preco as "Preço")))			  			
				from ementas where restaurantes.id_restaurante=ementas.id_restaurante))))
	from restaurantes INTO output;
	return output;
end;
$body$;

----EcraAdicionarRestaurante
--Inserir Restaurante

create or replace function InserirRestaurante(nome varchar(20),email varchar(50),telefone varchar(9),morada varchar(50)) returns integer 
LANGUAGE plpgsql
as $body$
declare
	n_sequencia integer;
begin
	insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT,nome,email,telefone,morada);
	select currval('seq_restaurantes') into n_sequencia;
	return n_sequencia;
end;
$body$;

--Inserir Locais de Consumo

create or replace function InserirLocalConsumo(id_restaurante integer,designacao varchar(15),lugares integer) returns boolean 
LANGUAGE plpgsql
as $body$
begin
	insert into locais_consumo (id_local_consumo, id_restaurante, designacao, numero_lugares) values (DEFAULT,id_restaurante,designacao,lugares);
	return 1;
end;
$body$;

----EcraRestaurante
--Preencher Dados do Restaurante

create or replace function SelecionarRestaurante(id_r integer) RETURNS TABLE (
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

----EcraAdicionarEmenta
--Preencher Itens

create or replace function SelecionarItens() RETURNS TABLE (
    id integer,
    designacao VARCHAR(50)
) 
LANGUAGE plpgsql
as $body$
begin
	return query select * from itens;
end;
$body$;

--Inserir Ementa

create or replace function InserirEmenta(id_r integer,designacao varchar(15),preco money,
																				tipo_refeicao varchar(15),tipo_ementa varchar(15),dia date) 
																				returns integer
LANGUAGE plpgsql
as $body$
declare
	id_tr integer;
	id_te integer;
	id_d integer;
	n_sequencia integer;
begin
	select id_tipo_refeicao into id_tr from tipo_refeicoes where tipo_refeicoes.designacao=tipo_refeicao;
	select id_tipo_ementa  into id_te from tipo_ementas where tipo_ementas.designacao=tipo_ementa;
	if exists (select * from datas where datas.data=dia) then
		select id_data into id_d from datas where datas.data=dia;
	end if;
	if not exists (select * from datas where datas.data=dia) then
		insert into datas(id_data,data) values (DEFAULT,dia);
		select id_data into id_d from datas where datas.data=dia;
	end if;
	Insert into ementas values
	(DEFAULT,id_r,id_te,id_tr,id_d,designacao,preco);
	
	select currval('seq_ementas') into n_sequencia;
	return n_sequencia;
end;
$body$;

--Inserir Itens da Ementa

create or replace function InserirItenEmenta(id_e integer,id_i integer)
																				returns integer
LANGUAGE plpgsql
as $body$
begin
	if not exists (select * from ementa_itens where ementa_itens.id_ementa=id_e and ementa_itens.id_iten) then
		insert into ementa_itens values (id_e,id_i);
	end if;
	return 1;
end;
$body$;

--Trigger Inserir ao Stock
create or replace function adicionar_item_stock() returns trigger
LANGUAGE plpgsql
as $body$
declare id_r integer;
begin
	select ementas.id_restaurante into id_r from ementas where ementas.id_ementa=NEW.id_ementa;
	if not exists (select * from stock where stock.id_restaurante=id_r and stock.id_iten=New.id_iten) then
		Insert into stock values (id_r,NEW.id_iten,0);
	end if;
	return NEW;
end;
$body$;

create trigger adicionar_item_stock
after insert on ementa_itens
for each row execute procedure adicionar_item_stock();

----EcraEmentas
--Preencher tree

create or replace function SelectEmentasRestaurante(id_r integer) RETURNS TABLE (
    id integer,
    designacao_ementa VARCHAR(15),
    designacao_tipo_ementa VARCHAR(15),
   	designacao_tipo_refeicao VARCHAR(15),
    dia date,
		preco money
) 
LANGUAGE plpgsql
as $body$
begin
	return query select * from mostrar_ementas where mostrar_ementas.id = ANY (select id_ementa from ementas where id_restaurante=id_r);
end;
$body$;

--View
create view mostrar_ementas
as select ementas.id_ementa as Id,ementas.designacao as "Designacao",tipo_ementas.designacao as "Tipo Ementa",
					tipo_refeicoes.designacao as "Tipo Refeicao",datas.data as "Data",ementas.preco as "Preco"
	from ementas join datas
		on ementas.id_data=datas.id_data join tipo_ementas
			on ementas.id_tipo_ementa=tipo_ementas.id_tipo_ementa join tipo_refeicoes
				on ementas.id_tipo_refeicao=tipo_refeicoes.id_tipo_refeicao
				
				
----EcraStock
--Preencher lista

create or replace function SelecionarStockRestaurante(id_r integer) RETURNS TABLE (
    id integer,
    designacao VARCHAR(50),
		quantidade integer
) 
LANGUAGE plpgsql
as $body$
begin
	return query select stock.id_iten,itens.designacao,stock.numero_itens
								from stock join itens
									on stock.id_iten=itens.id_iten
								where stock.id_restaurante=id_r;
end;
$body$;

--AlterarStock

create or replace function AlterarStockIten(id_r integer,id_i integer,quantidade integer) returns void
LANGUAGE plpgsql
as $body$
begin
		update stock
		set numero_itens=quantidade
		where id_restaurante=id_r and id_iten=id_i;
end;
$body$;



create or replace function SelectAlergias() RETURNS TABLE (
    id integer,
    designacao VARCHAR(50)
) 
LANGUAGE plpgsql
as $body$
begin
	return query select * from alergias;
end;
$body$;

