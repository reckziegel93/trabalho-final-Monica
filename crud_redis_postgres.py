import redis
import psycopg2

# ====== Conexão Redis ======
r = redis.Redis(host='localhost', port=6379, db=0)

# CRUD Redis
def redis_crud():
    # CREATE
    r.set('usuario:1', 'João')
    r.set('usuario:2', 'Maria')

    # READ
    print("Redis Read:", r.get('usuario:1').decode('utf-8'))

    # UPDATE
    r.set('usuario:1', 'João Silva')
    print("Redis Updated:", r.get('usuario:1').decode('utf-8'))

    # DELETE
    r.delete('usuario:2')
    print("Redis Keys after delete:", r.keys())

# ====== Conexão PostgreSQL ======
conn = psycopg2.connect(
    host="localhost",
    database="ProjetoConexao",
    user="postgres",
    password="unochapeco"
)
cur = conn.cursor()

# CRUD PostgreSQL
def postgres_crud():
    # CREATE tabela e inserir dados
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100)
        )
    """)
    conn.commit()
    
    cur.execute("INSERT INTO usuarios (nome) VALUES (%s)", ("João",))
    cur.execute("INSERT INTO usuarios (nome) VALUES (%s)", ("Maria",))
    conn.commit()

    # READ
    cur.execute("SELECT * FROM usuarios")
    print("PostgreSQL Read:", cur.fetchall())

    # UPDATE
    cur.execute("UPDATE usuarios SET nome=%s WHERE id=%s", ("João Silva", 1))
    conn.commit()
    cur.execute("SELECT * FROM usuarios")
    print("PostgreSQL Updated:", cur.fetchall())

    # DELETE
    cur.execute("DELETE FROM usuarios WHERE id=%s", (2,))
    conn.commit()
    cur.execute("SELECT * FROM usuarios")
    print("PostgreSQL after delete:", cur.fetchall())

# ====== Executar CRUDs ======
if __name__ == "__main__":
    print("==== REDIS CRUD ====")
    redis_crud()
    print("\n==== POSTGRESQL CRUD ====")
    postgres_crud()

# Fechar conexão PostgreSQL
cur.close()
conn.close()
