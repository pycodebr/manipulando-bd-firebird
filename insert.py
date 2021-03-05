import firebirdsql

# Conecta no seu BD #
con = firebirdsql.connect(
    host='127.0.0.1',
    database=r'dados.fdb',
    #port=3050,
    user='SYSDBA',
    password='masterkey' 
)

# Cria query, insere e dá commit no registro #
q = con.cursor()
q.execute("INSERT INTO CLIENTES (NOME, IDADE, SEXO) VALUES ('Felipe', 20, 'M')")
q.execute("INSERT INTO CLIENTES (NOME, IDADE, SEXO) VALUES ('Marcio', 40, 'M')")
q.execute("INSERT INTO CLIENTES (NOME, IDADE, SEXO) VALUES ('Maria', 23, 'F')")
con.commit()