/*==============================================================*/
/* SEQUENCIAS                                                   */
/*==============================================================*/

CREATE SEQUENCE seq_alergias START 1;
ALTER TABLE alergias ALTER COLUMN id_alergia SET DEFAULT nextval('seq_alergias');
ALTER TABLE alergias ALTER COLUMN id_alergia SET NOT NULL;
ALTER SEQUENCE seq_alergias OWNED BY alergias.id_alergia; 

CREATE SEQUENCE seq_clientes START 1;
ALTER TABLE clientes ALTER COLUMN id_cliente SET DEFAULT nextval('seq_clientes');
ALTER TABLE clientes ALTER COLUMN id_cliente SET NOT NULL;
ALTER SEQUENCE seq_clientes OWNED BY clientes.id_cliente; 

CREATE SEQUENCE seq_consumos START 1;
ALTER TABLE consumos ALTER COLUMN id_consumo SET DEFAULT nextval('seq_consumos');
ALTER TABLE consumos ALTER COLUMN id_consumo SET NOT NULL;
ALTER SEQUENCE seq_consumos OWNED BY consumos.id_consumo; 

CREATE SEQUENCE seq_datas START 1;
ALTER TABLE datas ALTER COLUMN id_data SET DEFAULT nextval('seq_datas');
ALTER TABLE datas ALTER COLUMN id_data SET NOT NULL;
ALTER SEQUENCE seq_datas OWNED BY datas.id_data; 

CREATE SEQUENCE seq_ementas START 1;
ALTER TABLE ementas ALTER COLUMN id_ementa SET DEFAULT nextval('seq_ementas');
ALTER TABLE ementas ALTER COLUMN id_ementa SET NOT NULL;
ALTER SEQUENCE seq_ementas OWNED BY ementas.id_ementa; 


CREATE SEQUENCE seq_itens START 1;
ALTER TABLE itens ALTER COLUMN id_iten SET DEFAULT nextval('seq_itens');
ALTER TABLE itens ALTER COLUMN id_iten SET NOT NULL;
ALTER SEQUENCE seq_itens OWNED BY itens.id_iten; 

CREATE SEQUENCE seq_locaisconsumo START 1;
ALTER TABLE locais_consumo ALTER COLUMN id_local_consumo SET DEFAULT nextval('seq_locaisconsumo');
ALTER TABLE locais_consumo ALTER COLUMN id_local_consumo SET NOT NULL;
ALTER SEQUENCE seq_locaisconsumo OWNED BY locais_consumo.id_local_consumo; 

CREATE SEQUENCE seq_restaurantes START 1;
ALTER TABLE restaurantes ALTER COLUMN id_restaurante SET DEFAULT nextval('seq_restaurantes');
ALTER TABLE restaurantes ALTER COLUMN id_restaurante SET NOT NULL;
ALTER SEQUENCE seq_restaurantes OWNED BY restaurantes.id_restaurante; 

/*==============================================================*/
/* Dados                                                   */
/*==============================================================*/

INSERT INTO tipo_refeicoes values (1,'Pequeno-Almoço');
INSERT INTO tipo_refeicoes values (2,'Almoço');
INSERT INTO tipo_refeicoes values (3,'Jantar');

INSERT INTO tipo_ementas values (2,'Entradas');
INSERT INTO tipo_ementas values (3,'Pratos de Peixe');
INSERT INTO tipo_ementas values (4,'Pratos de Carne');
INSERT INTO tipo_ementas values (5,'Sobremesas');

insert into alergias (id_alergia, designacao) values (DEFAULT, 'Pannariaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Tamaricaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Fabaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Asteraceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Poaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Cactaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Poaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Asteraceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Liliaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Dryopteridaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Rosaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Cyperaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Scrophulariaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Brassicaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Illiciaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Melastomataceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Fabaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Polygalaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Cyperaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Brachytheciaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Fabaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Solanaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Campanulaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Dryopteridaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Violaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Saxifragaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Fabaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Brassicaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Amaranthaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Poaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Nyctaginaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Chenopodiaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Liliaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Scrophulariaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Seligeriaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Lichinaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Lycopodiaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Rosaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Cyperaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Parmeliaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Asteraceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Rhamnaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Polygonaceae');
insert into alergias (id_alergia, designacao) values (DEFAULT, 'Gesneriaceae');

insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Centidel', 'cgiercke0@forbes.com', 910000001, '6531 Southridge Point');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Rhyloo', 'ccamilio1@techcrunch.com', 910000002, '052 Texas Point');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Topicware', 'vbeazer2@psu.edu', 910000003, '0448 Schmedeman Place');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Lazzy', 'rlinner3@twitter.com', 910000004, '37 Beilfuss Avenue');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Brightdog', 'dboick4@nsw.gov.au', 910000005, '93705 Tomscot Place');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Skipfire', 'iburtonshaw5@meetup.com', 910000006, '26 Dryden Place');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Tagopia', 'friccardini6@reference.com', 910000007, '243 Bluestem Way');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Oyope', 'amacallester7@facebook.com', 910000008, '3740 Loeprich Drive');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Edgewire', 'lbottinelli8@vimeo.com', 910000009, '39186 Pepper Wood Road');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Oyoba', 'jschmidt9@usda.gov', 910000010, '8089 Bluejay Parkway');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Kwimbee', 'wgemsona@epa.gov', 910000011, '3 Kropf Trail');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Skinix', 'rdennessb@163.com', 910000012, '4778 Susan Parkway');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Topicware', 'ubolensc@google.nl', 910000013, '5762 Gale Hill');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Flipstorm', 'dfilmerd@ucoz.com', 910000014, '3 Anthes Pass');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Mita', 'mtallmane@nasa.gov', 910000015, '3 Ludington Street');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Meevee', 'odewittf@discuz.net', 910000016, '066 Carpenter Point');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Twitterlist', 'cevettg@w3.org', 910000017, '9 Sunbrook Center');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Devshare', 'rluardh@gravatar.com', 910000018, '3 Kings Point');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Aivee', 'cwarehami@drupal.org', 910000019, '390 Sloan Hill');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Fanoodle', 'hquinneyj@ask.com', 910000020, '8 Fairview Place');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Skidoo', 'tjayesk@oakley.com', 910000021, '9427 Ridgeway Way');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Kaymbo', 'grupell@nps.gov', 910000022, '072 Armistice Lane');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Topicblab', 'bspurlingm@home.pl', 910000023, '220 Dwight Hill');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Dynazzy', 'gcasettin@ucoz.com', 910000024, '63 Waubesa Place');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Shufflester', 'fhusbando@fc2.com', 910000025, '3 Dwight Pass');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Dazzlesphere', 'tadanp@free.fr', 910000026, '35759 American Ash Parkway');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Thoughtbridge', 'ewickmannq@feedburner.com', 910000027, '7 Fairfield Lane');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Meeveo', 'abremleyr@japanpost.jp', 910000028, '5 Lyons Street');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Blogpad', 'wfagans@blog.com', 910000029, '495 Mesta Lane');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Oozz', 'lcrowchet@jalbum.net', 910000030, '3 High Crossing Street');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Gigabox', 'bferranu@blogtalkradio.com', 910000031, '8333 Cherokee Pass');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Eidel', 'aperingv@edublogs.org', 910000032, '440 Del Sol Way');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Skyba', 'lcrossgrovew@wikispaces.com', 910000033, '1 Judy Plaza');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Katz', 'ldodsx@who.int', 910000034, '356 Crowley Center');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Cogidoo', 'smerseyy@elpais.com', 910000035, '51810 Schiller Lane');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Innotype', 'gverricoz@mapquest.com', 910000036, '87542 Farragut Trail');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Jaxspan', 'wscourgie10@whitehouse.gov', 910000037, '863 Esker Center');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Livetube', 'plightbown11@google.fr', 910000038, '850 Union Junction');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Ozu', 'igarrould12@mozilla.com', 910000039, '07901 Clarendon Junction');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Quimm', 'zourry13@icio.us', 910000040, '324 Marcy Street');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Yoveo', 'ushepley14@nytimes.com', 910000041, '5 Arapahoe Junction');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Talane', 'hdockrell15@state.gov', 910000042, '7104 Utah Junction');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Skimia', 'krawson16@smugmug.com', 910000043, '25 Elgar Circle');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Trilith', 'jfernao17@people.com.cn', 910000044, '0102 Main Circle');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Bluejam', 'mklaaasen18@google.ru', 910000045, '3800 Alpine Way');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Skivee', 'eholmyard19@xinhuanet.com', 910000046, '5 Lerdahl Parkway');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Quaxo', 'cleclercq1a@mashable.com', 910000047, '7050 Stone Corner Center');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Dabvine', 'hbree1b@lycos.com', 910000048, '71 Quincy Court');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Podcat', 'ngiacobilio1c@nymag.com', 910000049, '0 Porter Pass');
insert into restaurantes (id_restaurante, nome, email, telefone, morada) values (DEFAULT, 'Skidoo', 'gdehooge1d@latimes.com', 910000050, '694 Mariners Cove Place');

insert into itens (id_iten, designacao) values (DEFAULT, 'Muffin Mix - Oatmeal');
insert into itens (id_iten, designacao) values (DEFAULT, 'Flour - Whole Wheat');
insert into itens (id_iten, designacao) values (DEFAULT, 'Roe - Flying Fish');
insert into itens (id_iten, designacao) values (DEFAULT, 'Pop - Club Soda Can');
insert into itens (id_iten, designacao) values (DEFAULT, 'Bar Special K');
insert into itens (id_iten, designacao) values (DEFAULT, 'Split Peas - Green, Dry');
insert into itens (id_iten, designacao) values (DEFAULT, 'Soup - Campbells, Creamy');
insert into itens (id_iten, designacao) values (DEFAULT, 'Spic And Span All Purpose');
insert into itens (id_iten, designacao) values (DEFAULT, 'Cheese - Provolone');
insert into itens (id_iten, designacao) values (DEFAULT, 'Wine - Prosecco Valdobiaddene');
insert into itens (id_iten, designacao) values (DEFAULT, 'Chicken - Leg / Back Attach');
insert into itens (id_iten, designacao) values (DEFAULT, 'Salt - Seasoned');
insert into itens (id_iten, designacao) values (DEFAULT, 'Flower - Potmums');
insert into itens (id_iten, designacao) values (DEFAULT, 'Filter - Coffee');
insert into itens (id_iten, designacao) values (DEFAULT, 'Raspberries - Frozen');
insert into itens (id_iten, designacao) values (DEFAULT, 'Doilies - 8, Paper');
insert into itens (id_iten, designacao) values (DEFAULT, 'Rice - Brown');
insert into itens (id_iten, designacao) values (DEFAULT, 'Wine - Winzer Krems Gruner');
insert into itens (id_iten, designacao) values (DEFAULT, 'Cheese Cloth No 60');
insert into itens (id_iten, designacao) values (DEFAULT, 'Jam - Strawberry, 20 Ml Jar');
insert into itens (id_iten, designacao) values (DEFAULT, 'Sobe - Orange Carrot');
insert into itens (id_iten, designacao) values (DEFAULT, 'Wine - Rosso Toscano Igt');
insert into itens (id_iten, designacao) values (DEFAULT, 'Soupcontfoam16oz 116con');
insert into itens (id_iten, designacao) values (DEFAULT, 'Sun - Dried Tomatoes');
insert into itens (id_iten, designacao) values (DEFAULT, 'Island Oasis - Magarita Mix');
insert into itens (id_iten, designacao) values (DEFAULT, 'Coconut Milk - Unsweetened');
insert into itens (id_iten, designacao) values (DEFAULT, 'Oven Mitt - 13 Inch');
insert into itens (id_iten, designacao) values (DEFAULT, 'Thyme - Dried');
insert into itens (id_iten, designacao) values (DEFAULT, 'Soup - Knorr, Chicken Noodle');
insert into itens (id_iten, designacao) values (DEFAULT, 'Fireball Whisky');
insert into itens (id_iten, designacao) values (DEFAULT, 'Wine - Lamancha Do Crianza');
insert into itens (id_iten, designacao) values (DEFAULT, 'Red Currants');
insert into itens (id_iten, designacao) values (DEFAULT, 'Shallots');
insert into itens (id_iten, designacao) values (DEFAULT, 'Red Pepper Paste');
insert into itens (id_iten, designacao) values (DEFAULT, 'Wine - Lamancha Do Crianza');
insert into itens (id_iten, designacao) values (DEFAULT, 'French Pastries');
insert into itens (id_iten, designacao) values (DEFAULT, 'Everfresh Products');
insert into itens (id_iten, designacao) values (DEFAULT, 'Cleaner - Bleach');
insert into itens (id_iten, designacao) values (DEFAULT, 'Bananas');
insert into itens (id_iten, designacao) values (DEFAULT, 'Wine - Beaujolais Villages');
insert into itens (id_iten, designacao) values (DEFAULT, 'Chives - Fresh');
insert into itens (id_iten, designacao) values (DEFAULT, 'Crab Brie In Phyllo');
insert into itens (id_iten, designacao) values (DEFAULT, 'Soup - Campbells, Creamy');
insert into itens (id_iten, designacao) values (DEFAULT, 'Chips Potato Reg 43g');
insert into itens (id_iten, designacao) values (DEFAULT, 'Squeeze Bottle');
insert into itens (id_iten, designacao) values (DEFAULT, 'Soup - Campbells');
insert into itens (id_iten, designacao) values (DEFAULT, 'Napkin - Cocktail,beige 2 - Ply');
insert into itens (id_iten, designacao) values (DEFAULT, 'Broom And Broom Rack White');
insert into itens (id_iten, designacao) values (DEFAULT, 'Bread - Dark Rye');
insert into itens (id_iten, designacao) values (DEFAULT, 'Cheese - Victor Et Berthold');


