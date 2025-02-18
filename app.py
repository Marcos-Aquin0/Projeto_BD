#bibliotecas utilizadas
import streamlit as st
import psycopg2
import pandas as pd

# Configuração da conexão com Supabase PostgreSQL
DB_HOST = "aws-0-sa-east-1.pooler.supabase.com"  
DB_NAME = "postgres"
DB_USER = "postgres.omadaxjkaslyxfdmiumo"
DB_PASS = "#FQPxrjAJS5wh9Q5"
DB_PORT = "6543"

# Função para conectar ao banco de dados
def get_db_connection():
    """ Conecta ao banco PostgreSQL no Supabase """
    # Tenta conectar ao banco de dados
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn # Retorna a conexão
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Configuração da página
st.title("Desastres no Estado de São Paulo")
st.subheader("Projeto de Banco de Dados 2024/2")
st.write("Este aplicativo permite consultar dados de um banco de dados PostgreSQL Supabase usando comandos SQL.")
st.subheader("Digite seu comando SQL abaixo:")

# Campo de texto para o comando SQL
sql_query = st.text_area("Comando SQL", height=200)

# Botão para executar a consulta
if st.button("Executar Consulta"):
    # Conectar ao banco de dados
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor() # Cria um cursor
            cur.execute(sql_query) # Executa o comando SQL
            
            # Verificar se a consulta é de leitura ou escrita
            if sql_query.strip().lower().startswith(("select", "with")):
                # Buscar os resultados e exibir como tabela
                data = cur.fetchall()
                columns = [desc[0] for desc in cur.description] # Nomes das colunas
                df = pd.DataFrame(data, columns=columns) # Cria um DataFrame
                st.dataframe(df) # Exibe o DataFrame
            else:
                # Para comandos CREATE, INSERT, UPDATE, DELETE
                conn.commit() # Confirma a transação
                st.success("Consulta executada com sucesso!")
            
            cur.close() # Fecha o cursor
            conn.close() # Fecha a conexão
        except Exception as e:
            st.error(f"Erro ao executar a consulta: {e}")
