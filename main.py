import traceback
import streamlit as st
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os
import pymssql
import uuid

# Carrega variáveis de ambiente
load_dotenv()

# Configurações do SQL Server
SQL_SERVER = os.getenv('SQL_SERVER')
SQL_DATABASE = os.getenv('SQL_DATABASE')
SQL_USER = os.getenv('SQL_USER')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')

# Configurações do Azure Blob
blobConnectionString = os.getenv('BLOB_CONNECTION_STRING')
blobContainerName = os.getenv('BLOB_CONTAINER_NAME')
blobAccountName = os.getenv('BLOB_ACCOUNT_NAME')

# Títulos do formulário
st.title('Cadastro de Produtos')

# Formulário de cadastro de produtos
product_name = st.text_input('Nome do Produto')
product_price = st.number_input('Preço do Produto', min_value=0.0, format='%f')
product_description = st.text_area('Descrição do Produto')
product_image = st.file_uploader('Imagem do Produto', type=['jpg', 'png', 'jpeg'])

# Função para upload
def upload_blob(file):
    if file is None:
        return None 
    
    blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
    container_client = blob_service_client.get_container_client(blobContainerName)
    blob_name = str(uuid.uuid4()) + file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(), overwrite=True)
    imagem_url = f"https://{blobAccountName}.blob.core.windows.net/{blobContainerName}/{blob_name}"
    return imagem_url

# Inserir produto no SQL
def insert_product(product_name, product_price, product_description, product_image):
    try:
        if product_image is None:
            raise ValueError("Nenhuma imagem foi enviada.")
        
        imagem_url = upload_blob(product_image)

        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Produtos (nome, descricao, preco, imagem_url) VALUES (%s, %s, %s, %s)", 
            (product_name, product_description, product_price, imagem_url)
        )
        conn.commit()
        conn.close()
        return True
    
    except Exception as e:
        st.error(f'Erro ao inserir produto: {e}')

        st.info("ERRO COMPLETO:")
        st.text(traceback.format_exc())

        return False

# Listar produtos do SQL
def list_products():
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor(as_dict=True)
        cursor.execute("SELECT * FROM Produtos")
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    except Exception as e:
        st.error(f'Erro ao listar produtos: {e}')

        st.info("ERRO COMPLETO:")
        st.text(traceback.format_exc())
        return []

# Tela de listagem
def list_products_screen():
    products = list_products()
    if products:
        cards_por_linha = 2
        for i in range(0, len(products), cards_por_linha):
            cols = st.columns(cards_por_linha)
            for j, product in enumerate(products[i:i+cards_por_linha]):
                col = cols[j]
                with col:
                    st.markdown(f"### {product['nome']}")
                    st.write(f"**Descrição**: {product['descricao']}")
                    st.write(f"**Preço**: {product['preco']:.2f}")
                    if product["imagem_url"]:
                        st.image(product["imagem_url"], width=200)
                    st.markdown("---")

    else:
        st.info("Nenhum produto foi encontrado")

if "listar_produtos" not in st.session_state:
    st.session_state.listar_produtos = False

# Botão Salvar Produto
if st.button('Salvar Produto'):
    sucesso = insert_product(product_name, product_price, product_description, product_image)
    if sucesso:
        st.success("Produto salvo com sucesso!")
    list_products_screen()

# Cabeçalho produtos
st.header('Produtos Cadastrados')

# Botão Listar Produtos
if st.button("Listar Produtos"):
    st.session_state.listar_produtos = True

if st.session_state.listar_produtos:
    list_products_screen()
    st.success("Produtos listados com sucesso!")