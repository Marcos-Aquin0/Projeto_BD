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

3. **Verifique as instalações:**
    ```sh
    python -c "import streamlit; import psycopg2; import pandas"
    ```

4. **Execute o Streamlit:**
    ```sh
    streamlit hello
    ```

Se ainda houver problemas com psycopg2, tente:
```sh
conda install -c anaconda psycopg2
```

Ou como última alternativa:
```sh
conda install -c conda-forge postgresql
pip install psycopg2-binary
```

