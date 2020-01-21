/*==============================================================*/
/* DBMS name:      PostgreSQL 8                                 */
/* Created on:     21/01/2020 14:25:05                          */
/*==============================================================*/


drop index ALERGIAS_PK;

drop table ALERGIAS;

drop index CLIENTES_PK;

drop table CLIENTES;

drop index LOCAL_DE_CONSUMO_FK;

drop index CONSUMO_FK;

drop index CONSUMOS_PK;

drop table CONSUMOS;

drop index O_QUE_CONSUMIU2_FK;

drop index O_QUE_CONSUMIU_FK;

drop index O_QUE_CONSUMIU_PK;

drop table CONSUMO_EMENTAS;

drop index DATAS_PK;

drop table DATAS;

drop index TIPO_DA_EMENTA_FK;

drop index TIPO_DE_REFEICAO_FK;

drop index DATA_FK;

drop index TEM_FK;

drop index EMENTAS_PK;

drop table EMENTAS;

drop index E_FEITO_COM2_FK;

drop index E_FEITO_COM_FK;

drop index E_FEITO_COM_PK;

drop table EMENTA_ITENS;

drop index ITENS_PK;

drop table ITENS;

drop index LOCAIS_FK;

drop index LOCAIS_CONSUMO_PK;

drop table LOCAIS_CONSUMO;

drop index RELATIONSHIP_6_FK;

drop index RELATIONSHIP_5_FK;

drop index RELATIONSHIP_5_PK;

drop table RELATIONSHIP_5;

drop index RESTAURANTES_PK;

drop table RESTAURANTES;

drop index ASSOCIATION_2_FK;

drop index ASSOCIATION_1_FK;

drop index ASSOCIATION_1_PK;

drop table STOCK;

drop index TIPO_EMENTAS_PK;

drop table TIPO_EMENTAS;

drop index TIPO_REFEICOES_PK;

drop table TIPO_REFEICOES;

/*==============================================================*/
/* Table: ALERGIAS                                              */
/*==============================================================*/
create table ALERGIAS (
   ID_ALERGIA           INT4                 not null,
   DESIGNACAO           VARCHAR(50)          not null,
   constraint PK_ALERGIAS primary key (ID_ALERGIA)
);

/*==============================================================*/
/* Index: ALERGIAS_PK                                           */
/*==============================================================*/
create unique index ALERGIAS_PK on ALERGIAS (
ID_ALERGIA
);

/*==============================================================*/
/* Table: CLIENTES                                              */
/*==============================================================*/
create table CLIENTES (
   ID_CLIENTE           INT4                 not null,
   NOME                 VARCHAR(20)          not null,
   NIF                  VARCHAR(9)           not null,
   constraint PK_CLIENTES primary key (ID_CLIENTE)
);

/*==============================================================*/
/* Index: CLIENTES_PK                                           */
/*==============================================================*/
create unique index CLIENTES_PK on CLIENTES (
ID_CLIENTE
);

/*==============================================================*/
/* Table: CONSUMOS                                              */
/*==============================================================*/
create table CONSUMOS (
   ID_CONSUMO           INT4                 not null,
   ID_CLIENTE           INT4                 not null,
   ID_LOCAL_CONSUMO     INT4                 not null,
   PRECO_TOTAL          MONEY                not null,
   constraint PK_CONSUMOS primary key (ID_CONSUMO)
);

/*==============================================================*/
/* Index: CONSUMOS_PK                                           */
/*==============================================================*/
create unique index CONSUMOS_PK on CONSUMOS (
ID_CONSUMO
);

/*==============================================================*/
/* Index: CONSUMO_FK                                            */
/*==============================================================*/
create  index CONSUMO_FK on CONSUMOS (
ID_CLIENTE
);

/*==============================================================*/
/* Index: LOCAL_DE_CONSUMO_FK                                   */
/*==============================================================*/
create  index LOCAL_DE_CONSUMO_FK on CONSUMOS (
ID_LOCAL_CONSUMO
);

/*==============================================================*/
/* Table: CONSUMO_EMENTAS                                       */
/*==============================================================*/
create table CONSUMO_EMENTAS (
   ID_CONSUMO           INT4                 not null,
   ID_EMENTA            INT4                 not null,
   constraint PK_CONSUMO_EMENTAS primary key (ID_CONSUMO, ID_EMENTA)
);

/*==============================================================*/
/* Index: O_QUE_CONSUMIU_PK                                     */
/*==============================================================*/
create unique index O_QUE_CONSUMIU_PK on CONSUMO_EMENTAS (
ID_CONSUMO,
ID_EMENTA
);

/*==============================================================*/
/* Index: O_QUE_CONSUMIU_FK                                     */
/*==============================================================*/
create  index O_QUE_CONSUMIU_FK on CONSUMO_EMENTAS (
ID_CONSUMO
);

/*==============================================================*/
/* Index: O_QUE_CONSUMIU2_FK                                    */
/*==============================================================*/
create  index O_QUE_CONSUMIU2_FK on CONSUMO_EMENTAS (
ID_EMENTA
);

/*==============================================================*/
/* Table: DATAS                                                 */
/*==============================================================*/
create table DATAS (
   ID_DATA              INT4                 not null,
   DATA                 DATE                 not null,
   constraint PK_DATAS primary key (ID_DATA)
);

/*==============================================================*/
/* Index: DATAS_PK                                              */
/*==============================================================*/
create unique index DATAS_PK on DATAS (
ID_DATA
);

/*==============================================================*/
/* Table: EMENTAS                                               */
/*==============================================================*/
create table EMENTAS (
   ID_EMENTA            INT4                 not null,
   ID_RESTAURANTE       INT4                 null,
   ID_TIPO_EMENTA       INT4                 not null,
   ID_TIPO_REFEICAO     INT4                 not null,
   ID_DATA              INT4                 not null,
   DESIGNACAO           VARCHAR(50)          not null,
   PRECO                MONEY                not null,
   constraint PK_EMENTAS primary key (ID_EMENTA)
);

/*==============================================================*/
/* Index: EMENTAS_PK                                            */
/*==============================================================*/
create unique index EMENTAS_PK on EMENTAS (
ID_EMENTA
);

/*==============================================================*/
/* Index: TEM_FK                                                */
/*==============================================================*/
create  index TEM_FK on EMENTAS (
ID_RESTAURANTE
);

/*==============================================================*/
/* Index: DATA_FK                                               */
/*==============================================================*/
create  index DATA_FK on EMENTAS (
ID_DATA
);

/*==============================================================*/
/* Index: TIPO_DE_REFEICAO_FK                                   */
/*==============================================================*/
create  index TIPO_DE_REFEICAO_FK on EMENTAS (
ID_TIPO_REFEICAO
);

/*==============================================================*/
/* Index: TIPO_DA_EMENTA_FK                                     */
/*==============================================================*/
create  index TIPO_DA_EMENTA_FK on EMENTAS (
ID_TIPO_EMENTA
);

/*==============================================================*/
/* Table: EMENTA_ITENS                                          */
/*==============================================================*/
create table EMENTA_ITENS (
   ID_EMENTA            INT4                 not null,
   ID_ITEN              INT4                 not null,
   constraint PK_EMENTA_ITENS primary key (ID_EMENTA, ID_ITEN)
);

/*==============================================================*/
/* Index: E_FEITO_COM_PK                                        */
/*==============================================================*/
create unique index E_FEITO_COM_PK on EMENTA_ITENS (
ID_EMENTA,
ID_ITEN
);

/*==============================================================*/
/* Index: E_FEITO_COM_FK                                        */
/*==============================================================*/
create  index E_FEITO_COM_FK on EMENTA_ITENS (
ID_EMENTA
);

/*==============================================================*/
/* Index: E_FEITO_COM2_FK                                       */
/*==============================================================*/
create  index E_FEITO_COM2_FK on EMENTA_ITENS (
ID_ITEN
);

/*==============================================================*/
/* Table: ITENS                                                 */
/*==============================================================*/
create table ITENS (
   ID_ITEN              INT4                 not null,
   DESIGNACAO           VARCHAR(50)          not null,
   constraint PK_ITENS primary key (ID_ITEN)
);

/*==============================================================*/
/* Index: ITENS_PK                                              */
/*==============================================================*/
create unique index ITENS_PK on ITENS (
ID_ITEN
);

/*==============================================================*/
/* Table: LOCAIS_CONSUMO                                        */
/*==============================================================*/
create table LOCAIS_CONSUMO (
   ID_LOCAL_CONSUMO     INT4                 not null,
   ID_RESTAURANTE       INT4                 not null,
   DESIGNACAO           VARCHAR(50)          not null,
   NUMERO_LUGARES       INT4                 not null,
   constraint PK_LOCAIS_CONSUMO primary key (ID_LOCAL_CONSUMO)
);

/*==============================================================*/
/* Index: LOCAIS_CONSUMO_PK                                     */
/*==============================================================*/
create unique index LOCAIS_CONSUMO_PK on LOCAIS_CONSUMO (
ID_LOCAL_CONSUMO
);

/*==============================================================*/
/* Index: LOCAIS_FK                                             */
/*==============================================================*/
create  index LOCAIS_FK on LOCAIS_CONSUMO (
ID_RESTAURANTE
);

/*==============================================================*/
/* Table: RELATIONSHIP_5                                        */
/*==============================================================*/
create table RELATIONSHIP_5 (
   ID_ITEN              INT4                 not null,
   ID_ALERGIA           INT4                 not null,
   constraint PK_RELATIONSHIP_5 primary key (ID_ITEN, ID_ALERGIA)
);

/*==============================================================*/
/* Index: RELATIONSHIP_5_PK                                     */
/*==============================================================*/
create unique index RELATIONSHIP_5_PK on RELATIONSHIP_5 (
ID_ITEN,
ID_ALERGIA
);

/*==============================================================*/
/* Index: RELATIONSHIP_5_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_5_FK on RELATIONSHIP_5 (
ID_ITEN
);

/*==============================================================*/
/* Index: RELATIONSHIP_6_FK                                     */
/*==============================================================*/
create  index RELATIONSHIP_6_FK on RELATIONSHIP_5 (
ID_ALERGIA
);

/*==============================================================*/
/* Table: RESTAURANTES                                          */
/*==============================================================*/
create table RESTAURANTES (
   ID_RESTAURANTE       INT4                 not null,
   NOME                 VARCHAR(20)          not null,
   EMAIL                VARCHAR(50)          not null,
   TELEFONE             VARCHAR(9)           not null,
   MORADA               VARCHAR(50)          not null,
   constraint PK_RESTAURANTES primary key (ID_RESTAURANTE)
);

/*==============================================================*/
/* Index: RESTAURANTES_PK                                       */
/*==============================================================*/
create unique index RESTAURANTES_PK on RESTAURANTES (
ID_RESTAURANTE
);

/*==============================================================*/
/* Table: STOCK                                                 */
/*==============================================================*/
create table STOCK (
   ID_RESTAURANTE       INT4                 not null,
   ID_ITEN              INT4                 not null,
   NUMBERO_ITENS        INT4                 null,
   constraint PK_STOCK primary key (ID_RESTAURANTE, ID_ITEN)
);

/*==============================================================*/
/* Index: ASSOCIATION_1_PK                                      */
/*==============================================================*/
create unique index ASSOCIATION_1_PK on STOCK (
ID_RESTAURANTE,
ID_ITEN
);

/*==============================================================*/
/* Index: ASSOCIATION_1_FK                                      */
/*==============================================================*/
create  index ASSOCIATION_1_FK on STOCK (
ID_RESTAURANTE
);

/*==============================================================*/
/* Index: ASSOCIATION_2_FK                                      */
/*==============================================================*/
create  index ASSOCIATION_2_FK on STOCK (
ID_ITEN
);

/*==============================================================*/
/* Table: TIPO_EMENTAS                                          */
/*==============================================================*/
create table TIPO_EMENTAS (
   ID_TIPO_EMENTA       INT4                 not null,
   DESIGNACAO           VARCHAR(50)          not null,
   constraint PK_TIPO_EMENTAS primary key (ID_TIPO_EMENTA)
);

/*==============================================================*/
/* Index: TIPO_EMENTAS_PK                                       */
/*==============================================================*/
create unique index TIPO_EMENTAS_PK on TIPO_EMENTAS (
ID_TIPO_EMENTA
);

/*==============================================================*/
/* Table: TIPO_REFEICOES                                        */
/*==============================================================*/
create table TIPO_REFEICOES (
   ID_TIPO_REFEICAO     INT4                 not null,
   DESIGNACAO           VARCHAR(50)          not null,
   constraint PK_TIPO_REFEICOES primary key (ID_TIPO_REFEICAO)
);

/*==============================================================*/
/* Index: TIPO_REFEICOES_PK                                     */
/*==============================================================*/
create unique index TIPO_REFEICOES_PK on TIPO_REFEICOES (
ID_TIPO_REFEICAO
);

alter table CONSUMOS
   add constraint FK_CONSUMOS_CONSUMO_CLIENTES foreign key (ID_CLIENTE)
      references CLIENTES (ID_CLIENTE)
      on delete restrict on update restrict;

alter table CONSUMOS
   add constraint FK_CONSUMOS_LOCAL_DE__LOCAIS_C foreign key (ID_LOCAL_CONSUMO)
      references LOCAIS_CONSUMO (ID_LOCAL_CONSUMO)
      on delete restrict on update restrict;

alter table CONSUMO_EMENTAS
   add constraint FK_CONSUMO__O_QUE_CON_CONSUMOS foreign key (ID_CONSUMO)
      references CONSUMOS (ID_CONSUMO)
      on delete restrict on update restrict;

alter table CONSUMO_EMENTAS
   add constraint FK_CONSUMO__O_QUE_CON_EMENTAS foreign key (ID_EMENTA)
      references EMENTAS (ID_EMENTA)
      on delete restrict on update restrict;

alter table EMENTAS
   add constraint FK_EMENTAS_DATA_DATAS foreign key (ID_DATA)
      references DATAS (ID_DATA)
      on delete restrict on update restrict;

alter table EMENTAS
   add constraint FK_EMENTAS_TEM_RESTAURA foreign key (ID_RESTAURANTE)
      references RESTAURANTES (ID_RESTAURANTE)
      on delete restrict on update restrict;

alter table EMENTAS
   add constraint FK_EMENTAS_TIPO_DA_E_TIPO_EME foreign key (ID_TIPO_EMENTA)
      references TIPO_EMENTAS (ID_TIPO_EMENTA)
      on delete restrict on update restrict;

alter table EMENTAS
   add constraint FK_EMENTAS_TIPO_DE_R_TIPO_REF foreign key (ID_TIPO_REFEICAO)
      references TIPO_REFEICOES (ID_TIPO_REFEICAO)
      on delete restrict on update restrict;

alter table EMENTA_ITENS
   add constraint FK_EMENTA_I_E_FEITO_C_EMENTAS foreign key (ID_EMENTA)
      references EMENTAS (ID_EMENTA)
      on delete restrict on update restrict;

alter table EMENTA_ITENS
   add constraint FK_EMENTA_I_E_FEITO_C_ITENS foreign key (ID_ITEN)
      references ITENS (ID_ITEN)
      on delete restrict on update restrict;

alter table LOCAIS_CONSUMO
   add constraint FK_LOCAIS_C_LOCAIS_RESTAURA foreign key (ID_RESTAURANTE)
      references RESTAURANTES (ID_RESTAURANTE)
      on delete restrict on update restrict;

alter table RELATIONSHIP_5
   add constraint FK_RELATION_RELATIONS_ITENS foreign key (ID_ITEN)
      references ITENS (ID_ITEN)
      on delete restrict on update restrict;

alter table RELATIONSHIP_5
   add constraint FK_RELATION_RELATIONS_ALERGIAS foreign key (ID_ALERGIA)
      references ALERGIAS (ID_ALERGIA)
      on delete restrict on update restrict;

alter table STOCK
   add constraint FK_STOCK_STOCK_RESTAURA foreign key (ID_RESTAURANTE)
      references RESTAURANTES (ID_RESTAURANTE)
      on delete restrict on update restrict;

alter table STOCK
   add constraint FK_STOCK_STOCK2_ITENS foreign key (ID_ITEN)
      references ITENS (ID_ITEN)
      on delete restrict on update restrict;

