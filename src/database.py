import psycopg2

class Database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="brian",  
                host="127.0.0.1",
                port="5432"
            )
            print("Conectado ao banco com sucesso!")

            #  linha importante: define o schema padrão
            cur = self.conn.cursor()
            cur.execute("SET search_path TO public;")
            cur.close()

        except Exception as e:
            print("Erro ao conectar ao banco:", e)
            raise

    def consultar(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            resultados = cur.fetchall()
            cur.close()
            return resultados
        except Exception as e:
            print("Erro na consulta:", e)
            return []

    def fechar(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")
