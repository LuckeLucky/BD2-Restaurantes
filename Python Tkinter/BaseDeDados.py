import psycopg2

conn = psycopg2.connect(host="localhost", database="Restaurantes", user="postgres", password="reymisterio")
cur = conn.cursor()


def SelectRestaurantes():
    cur.callproc("SelectRestaurantes")
    data = cur.fetchall()
    return data


def SelectRestaurante(id):
    cur.callproc("SelectRestaurante", [str(id), ])
    data = cur.fetchall()
    return data


def SelectEmentasRestaurante(id):
    cur.callproc("SelectEmentasRestaurante", [str(id), ])
    data = cur.fetchall()
    return data


def InserirRestaurante(nome, email, telefone, morada):
    cur.callproc("InsertRestaurante", [nome, email, telefone, morada])
    data = cur.fetchone()[0]
    conn.commit()
    return data


def SearchRestaurante(str):
    cur.callproc("SearchRestaurante", [str, ])
    data = cur.fetchall()
    return data


def SelectItens():
    cur.callproc("SelectItens")
    data = cur.fetchall()
    return data


def InserirLocalConsumo(id_restaurante, designacao, lugares):
    cur.callproc("InserirLocalConsumo", [id_restaurante, designacao, lugares])
    conn.commit()


def SelecionarRestaurantes(pesquisa,ordem,sentido):
    cur.callproc("SelecionarRestaurantes", [pesquisa,ordem,sentido ])
    data = cur.fetchall()
    return data
