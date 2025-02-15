import streamlit as st
import mysql.connector as mariadb
import os

DATABASE = "database.db"

DB_CONFIG = {
    "host": "sql.freedb.tech",      # Mude para o IP do seu servidor, se necessário
    "port": 3306,             # Porta padrão do MariaDB
    "user": "freedb_tassin",    # Seu usuário do banco
    "password": "CY$$E%wCDNv7PS#",  # Sua senha do banco
    "database": "freedb_tassocaneladefogo"   # Nome do banco de dados
}

def get_db_connection():
    try:
        conn = mariadb.connect(**DB_CONFIG)
        return conn
    except mariadb.Error as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

st.title("Dados sobre desastres no Estado de São Paulo")
st.subheader("Projeto de Banco de Dados 2024/2")
st.write("É necessário estar conectado à internet da unifesp para acessar o banco de dados.")

# Área para digitar a consulta SQL
query = st.text_area("Digite sua consulta SQL", height=150)

if st.button("Executar Comando SQL"):
    try:
        conn = get_db_connection()
        if conn is None:
            raise Exception("Falha na conexão com o banco de dados.")
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        
        # Se for uma consulta SELECT, exibe os resultados
        if query.strip().lower().startswith("select"):
            results = cursor.fetchall()
            if results:
                # Converte os resultados em uma lista de dicionários
                data = [dict(row) for row in results]
                st.write("### Resultados:")
                st.dataframe(data)
            else:
                st.info("Nenhum resultado para exibir.")
        else:
            conn.commit()
            if query.strip().lower().startswith("insert"):
                st.success("Dados inseridos com sucesso!")
            elif query.strip().lower().startswith("update"):
                st.success("Dados atualizados com sucesso!")
            elif query.strip().lower().startswith("delete"):
                st.success("Dados deletados com sucesso!")
            elif query.strip().lower().startswith("create"):
                st.success("Tabela criada com sucesso!")
            else:
                st.success("Consulta executada com sucesso!")
        conn.close()
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")