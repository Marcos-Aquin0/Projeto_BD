import streamlit as st
import mariadb
import os

DATABASE = "database.db"
DB_CONFIG = {
    "host": "codd.unifesp.br",      # Mude para o IP do seu servidor, se necessário
    "port": 3306,             # Porta padrão do MariaDB
    "user": "alunobd",    # Seu usuário do banco
    "password": "alunobd",  # Sua senha do banco
    "database": "MarcosAquino"   # Nome do banco de dados
}
def get_db_connection():
    conn = mariadb.connect(**DB_CONFIG)
    conn.row_factory = mariadb.Row
    return conn

def init_db():
    """Inicializa o banco de dados com uma tabela de exemplo, se não existir."""
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER
            );
        ''')
        # Inserindo dados de exemplo
        cur.execute("INSERT INTO pessoas (nome, idade) VALUES ('Alice', 30)")
        cur.execute("INSERT INTO pessoas (nome, idade) VALUES ('Bruno', 25)")
        cur.execute("INSERT INTO pessoas (nome, idade) VALUES ('Carla', 28)")
        conn.commit()
        conn.close()

# Inicializa o banco de dados
init_db()

st.title("Interface de Consulta SQL com Streamlit")

# Área para digitar a consulta SQL
query = st.text_area("Digite sua consulta SQL", height=150)

if st.button("Executar Consulta"):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query)
        
        # Se for uma consulta SELECT, exibe os resultados
        if query.strip().lower().startswith("select"):
            results = cur.fetchall()
            if results:
                # Obtém os nomes das colunas
                columns = results[0].keys()
                # Converte os resultados em uma lista de dicionários
                data = [dict(row) for row in results]
                st.write("### Resultados:")
                st.dataframe(data)
            else:
                st.info("Nenhum resultado para exibir.")
        else:
            conn.commit()
            st.success("Consulta executada com sucesso!")
        conn.close()
    except Exception as e:
        st.error(f"Erro: {e}")
