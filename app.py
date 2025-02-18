import streamlit as st
import psycopg2
import pandas as pd

import os

# Carrega as variáveis de ambiente do arquivo .env

DB_HOST = st.secrets["postgres"]["DB_HOST"]
DB_NAME = st.secrets["postgres"]["DB_NAME"]
DB_USER = st.secrets["postgres"]["DB_USER"]
DB_PASS = st.secrets["postgres"]["DB_PASS"]
DB_PORT = st.secrets["postgres"]["DB_PORT"]

# Configuração da conexão com Supabase PostgreSQL
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "port": os.getenv("DB_PORT")
}

def get_db_connection():
    """ Conecta ao banco PostgreSQL no Supabase """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

st.title("Consulta ao Banco de Dados MongoDB Atlas")
st.subheader("Projeto de Banco de Dados 2024/2")
st.write("Este aplicativo permite consultar dados de um banco de dados PostgreSQL Supabase usando comandos SQL.")
st.subheader("Digite seu comando SQL abaixo:")

sql_query = st.text_area("Comando SQL", height=300)

if st.button("Executar Consulta"):
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(sql_query)
            
            if sql_query.strip().lower().startswith(("select", "with")):
                # Buscar os resultados e exibir como tabela
                data = cur.fetchall()
                columns = [desc[0] for desc in cur.description]
                df = pd.DataFrame(data, columns=columns)
                st.dataframe(df)
            else:
                # Para comandos CREATE, INSERT, UPDATE, DELETE
                conn.commit()
                st.success("Consulta executada com sucesso!")
            
            cur.close()
            conn.close()
        except Exception as e:
            st.error(f"Erro ao executar a consulta: {e}")
