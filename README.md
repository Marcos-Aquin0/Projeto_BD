# Projeto_BD
 Interface Gráfica desenvolvida para o projeto em grupo de Banco de Dados - Unifesp/SJC - 2024/2

# Instalando Dependências com Conda

1. **Crie e ative um novo ambiente conda:**
    ```sh
    conda create --name myenv python=3.8
    conda activate myenv
    ```

2. **Instale todas as dependências usando conda:**
    ```sh
    conda install -c conda-forge streamlit
    conda install -c conda-forge psycopg2
    conda install -c conda-forge pandas
    ```

# Executando app.py com Streamlit

Para executar o `app.py` usando Streamlit, siga estes passos:

1. **Navegue até o diretório que contém `app.py`:**
    ```sh
    cd ./Projeto_BD
    ```

2. **Execute o aplicativo Streamlit:**
    ```sh
    streamlit run app.py
    ```

3. **Abra a URL fornecida no seu navegador web:**

    Após executar o comando, o Streamlit fornecerá uma URL local (geralmente `http://localhost:8501`). Abra essa URL no seu navegador web para visualizar e interagir com o aplicativo. Ou utilize o deploy do streamlit 'https://projetobd2024-2.streamlit.app' 
