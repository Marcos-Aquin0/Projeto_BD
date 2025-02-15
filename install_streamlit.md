# Instalando Streamlit com Conda

Para instalar o Streamlit usando Conda, siga estes passos:

1. **Crie um novo ambiente Conda (opcional, mas recomendado):**
    ```sh
    conda create --name myenv python=3.8
    conda activate myenv
    ```

2. **Instale o Streamlit:**
    ```sh
    conda install -c conda-forge streamlit
    ```

3. **Verifique a instalação:**
    ```sh
    streamlit hello
    ```

Isso abrirá uma nova aba no seu navegador web padrão com o aplicativo hello world do Streamlit.

4. **Instale o MYSQL:**
    ```sh
    conda install mysql-connector-python
    ```

