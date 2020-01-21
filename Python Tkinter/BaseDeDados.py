import psycopg2


# EcraInicial
# Preencher Treeview
def SelecionarRestaurantes(pesquisa, ordem, sentido):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("SelecionarRestaurantes", [pesquisa, ordem, sentido])
    data = cur.fetchall()
    conn.close()
    return data


# EcraAdicionarRestaurante
# Inserir Restaurante
def InserirRestaurante(nome, email, telefone, morada):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("InserirRestaurante", [nome, email, telefone, morada])
    data = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return data


# Inserir Locais de Consumo
def InserirLocalConsumo(id_restaurante, designacao, lugares):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("InserirLocalConsumo", [id_restaurante, designacao, lugares])
    conn.commit()
    conn.close()


# EcraRestaurante
# Preencher Dados do Restaurante
def SelecionarRestaurante(id):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("SelecionarRestaurante", [str(id), ])
    data = cur.fetchall()
    conn.close()
    return data


# Exportar XML
def ExportarXML():
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("ExportarXML")
    data = cur.fetchone()[0]
    conn.close()
    return data


# EcraAdicionarEmenta
# Selecionar Itens
def SelecionarItens():
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("SelecionarItens")
    data = cur.fetchall()
    conn.close()
    return data


# Inserir Ementa
def InserirEmenta(id_restaurante, designacao, preco, tipo_refeicao, tipo_ementa, data):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("InserirEmenta", [str(id_restaurante), designacao, preco, tipo_refeicao, tipo_ementa, data])
    data = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return data


# Inserir Iten
def InserirItenEmenta(id_ementa, id_iten):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("InserirItenEmenta", [str(id_ementa), str(id_iten)])
    conn.commit()
    conn.close()


# EcraEmentas
# Preencher Treeview
def SelectEmentasRestaurante(id):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("SelectEmentasRestaurante", [str(id), ])
    data = cur.fetchall()
    conn.close()
    return data


# EcraStock
# Preencher lista stock
def SelecionarStockRestaurante(id):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("SelecionarStockRestaurante", [str(id), ])
    data = cur.fetchall()
    conn.close()
    return data


# Alterar Stock
def AlterarStockIten(id_restaurante, id_iten, quantidade):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("AlterarStockIten", [str(id_restaurante), str(id_iten), str(quantidade)])
    conn.commit()
    conn.close()


# EcraAdicionarConsumo
# Preenche Locais de Consumo
def SelecionarLocaisConsumoRestaurante(id_restaurante):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("SelecionarLocaisConsumoRestaurante", [str(id_restaurante), ])
    data = cur.fetchall()
    conn.close()
    return data


# Preenche lista de Ementas
def SelecionarEmentasDisponiveis(id_restaurante, tipo_ementa, tipo_refeicao):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("SelecionarEmentasDisponiveis", [str(id_restaurante), tipo_ementa, tipo_refeicao])
    data = cur.fetchall()
    conn.close()
    return data


# Mostrar Alergias da Ementa
def AlergiasEmenta(id_ementa):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("AlergiasEmenta", [str(id_ementa)])
    data = cur.fetchone()[0]
    conn.close()
    return data


# Actualizar o stock da ementa
def ConsumirEmenta(id_restaurante, id_ementa):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("ConsumirEmenta", [str(id_restaurante), str(id_ementa)])
    data = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return data


# Inserir Consumo
def InserirConsumo(id_restaurante, nome_cliente, nif_cliente, nome_local, lugares, preco):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("InserirConsumo", [str(id_restaurante), nome_cliente, nif_cliente, nome_local, lugares, str(preco)])
    data = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return data


# Inserir Consumo Ementa
def InserirConsumoEmenta(id_consumo, id_ementa):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("InserirConsumoEmenta", [str(id_consumo), str(id_ementa)])
    conn.commit()
    conn.close()


# Retirar consumo
def DeConsumirEmenta(id_restaurante, id_ementa):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("DeConsumirEmenta", [str(id_restaurante), str(id_ementa)])
    conn.commit()
    conn.close()


# EcraAdicionarItem
# SelecionarAlergias
def SelecionarAlergias():
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("SelecionarAlergias")
    data = cur.fetchall()
    conn.close()
    return data


# Adicionar Nova Alergia
def InserirAlergia(nome):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("InserirAlergia", [nome])
    conn.commit()
    conn.close()


# Inserir Iten
def InserirIten(nome):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("InserirIten", [nome])
    data = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return data


# Inserir Alergia Iten
def InserirAlergiaIten(id_iten, nome_alergia):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("InserirAlergiaIten", [str(id_iten), nome_alergia])
    conn.commit()
    conn.close()


# EcraEditarRestaurante
# Alterar Restaurante
def AlterarRestaurante(id_restaurante, nome, email, telefone, morada):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("AlterarRestaurante", [str(id_restaurante), nome, email, telefone, morada])
    conn.commit()
    conn.close()


# Apagar Restaurante
def ApagarRestaurante(id_restaurante):
    conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
    cur = conn.cursor()
    cur.callproc("ApagarRestaurante", [str(id_restaurante)])
    conn.commit()
    conn.close()

