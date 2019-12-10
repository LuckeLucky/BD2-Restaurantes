import psycopg2

class basededados():
    def connect(self):
        conn = psycopg2.connect(host="192.168.43.13",database="Restaurante", user="R&R_admin", password="estgv16790")
        cur = conn.cursor()
        cur.execute("select * from restaurantes limit 10")
        conn.close()

 

