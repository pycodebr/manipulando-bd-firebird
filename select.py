import firebirdsql

# Conecta no seu BD #
con = firebirdsql.connect(
    host='127.0.0.1',
    database=r'dados.fdb',
    #port=3050,
    user='SYSDBA',
    password='masterkey' 
)

# Cria query, seleciona os registros e os mostra #
q = con.cursor()
q.execute("SELECT * FROM CLIENTES")
clientes = q.fetchall()
print(clientes)