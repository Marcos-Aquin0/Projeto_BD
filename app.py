import streamlit as st
import psycopg2
import pandas as pd

# Configuração da conexão com Supabase PostgreSQL
DB_HOST = "aws-0-sa-east-1.pooler.supabase.com"  # Pegue no painel do Supabase
DB_NAME = "postgres"
DB_USER = "postgres.omadaxjkaslyxfdmiumo"
DB_PASS = "#FQPxrjAJS5wh9Q5"
DB_PORT = "6543"

def get_db_connection():
    """ Conecta ao banco PostgreSQL no Supabase """
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

st.title("Desastres no Estado de São Paulo")
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
