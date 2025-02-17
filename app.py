import streamlit as st
from pymongo import MongoClient

# Configurações do MongoDB Atlas
MONGO_URI = "mongodb+srv://marcosaquinoic:gGtPTFngmkeBtOKm@tassinbd.bi0zn.mongodb.net/?retryWrites=true&w=majority&appName=TassinBD"  # Substitua pela sua string de conexão
DATABASE_NAME = "TassinBD"  # Substitua pelo nome do banco de dados
COLLECTION_NAME = "projetobd"  # Substitua pelo nome da coleção

# Função para conectar ao MongoDB
def get_db_connection():
    try:
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        return collection
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

st.title("Consulta ao Banco de Dados MongoDB Atlas")
st.subheader("Projeto de Banco de Dados 2024/2")
st.write("Este aplicativo permite consultar dados de um banco de dados MongoDB Atlas.")

# Área para digitar a consulta (filtro) no formato JSON
query = st.text_area("Digite sua consulta (filtro) no formato JSON", height=100, value='{}')

if st.button("Executar Consulta"):
    try:
        collection = get_db_connection()
        if collection is None:
            raise Exception("Falha na conexão com o banco de dados.")
        
        # Converte a consulta de string JSON para um dicionário Python
        query_dict = eval(query)
        
        # Executa a consulta no MongoDB
        results = list(collection.find(query_dict))
        
        if results:
            st.write("### Resultados:")
            st.write(results)  # Exibe os resultados brutos
        else:
            st.info("Nenhum resultado para exibir.")
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")