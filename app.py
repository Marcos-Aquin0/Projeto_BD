import streamlit as st
import psycopg2
import pandas as pd

# Configuração da conexão com Supabase PostgreSQL usando st.secrets
DB_CONFIG = {
    "host": st.secrets["postgres"]["DB_HOST"],
    "dbname": st.secrets["postgres"]["DB_NAME"],
    "user": st.secrets["postgres"]["DB_USER"],
    "password": st.secrets["postgres"]["DB_PASS"],
    "port": st.secrets["postgres"]["DB_PORT"]
}

def get_db_connection():
    """ Conecta ao banco PostgreSQL no Supabase """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
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
