import psycopg2

conn = psycopg2.connect(host="localhost",database="Restaurantes", user="postgres", password="reymisterio")
cur = conn.cursor()
    

def SelectRestaurantes():

    cur.callproc("SelectRestaurantes")
    data = cur.fetchall()
    return data

def SelectRestaurante(id):

    cur.callproc("SelectRestaurante",[str(id),])
    data = cur.fetchall()
    return data

def SelectEmentasRestaurante(id):

    cur.callproc("SelectEmentasRestaurante",[str(id),])
    data = cur.fetchall()
    return data

def InsertRestaurante(nome,email,telefone,morada):
    cur.callproc("InsertRestaurante",[nome,email,telefone,morada])
    conn.commit()

def SearchRestaurante(str):

    cur.callproc("SearchRestaurante",[str,])
    data = cur.fetchall()
    return data

def SelectItens(str):
    
    cur.callproc("SelectItens")
    data = cur.fetchall()
    return data
 

