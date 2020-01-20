import psycopg2

conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
cur = conn.cursor()


# EcraInicial
# Preencher Treeview
def SelecionarRestaurantes(pesquisa, ordem, sentido):
    cur.callproc("SelecionarRestaurantes", [pesquisa, ordem, sentido])
    data = cur.fetchall()
    return data


# EcraAdicionarRestaurante
# Inserir Restaurante
def InserirRestaurante(nome, email, telefone, morada):
    cur.callproc("InserirRestaurante", [nome, email, telefone, morada])
    data = cur.fetchone()[0]
    conn.commit()
    return data


# Inserir Locais de Consumo
def InserirLocalConsumo(id_restaurante, designacao, lugares):
    cur.callproc("InserirLocalConsumo", [id_restaurante, designacao, lugares])
    conn.commit()


# EcraRestaurante
# Preencher Dados do Restaurante
def SelecionarRestaurante(id):
    cur.callproc("SelecionarRestaurante", [str(id), ])
    data = cur.fetchall()
    return data


# Exportar XML
def ExportarXML():
    cur.callproc("ExportarXML")
    data = cur.fetchone()[0]
    return data


# EcraAdicionarEmenta
# Selecionar Itens
def SelecionarItens():
    cur.callproc("SelecionarItens")
    data = cur.fetchall()
    return data


# Inserir Ementa
def InserirEmenta(id_restaurante, designacao, preco, tipo_refeicao, tipo_ementa, data):
    cur.callproc("InserirEmenta", [str(id_restaurante), designacao, preco, tipo_refeicao, tipo_ementa, data])
    data = cur.fetchone()[0]
    conn.commit()
    return data


# Inserir Iten
def InserirItenEmenta(id_ementa, id_iten):
    cur.callproc("InserirItenEmenta", [str(id_ementa), str(id_iten)])
    conn.commit()


# EcraEmentas
# Preencher Treeview
def SelectEmentasRestaurante(id):
    cur.callproc("SelectEmentasRestaurante", [str(id), ])
    data = cur.fetchall()
    return data


# EcraStock
# Preencher lista stock
def SelecionarStockRestaurante(id):
    cur.callproc("SelecionarStockRestaurante", [str(id), ])
    data = cur.fetchall()
    return data


# Alterar Stock
def AlterarStockIten(id_restaurante, id_iten, quantidade):
    cur.callproc("AlterarStockIten", [str(id_restaurante), str(id_iten), str(quantidade)])
    conn.commit()


# EcraAdicionarConsumo
# Preenche Locais de Consumo
def SelecionarLocaisConsumoRestaurante(id_restaurante):
    cur.callproc("SelecionarLocaisConsumoRestaurante", [str(id_restaurante), ])
    data = cur.fetchall()
    return data


# Preenche lista de Ementas



def SelectAlergias():
    cur.callproc("SelectAlergias")
    data = cur.fetchall()
    return data
