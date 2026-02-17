# Projeto de Armazenamento de um E-Commerce na Cloud Azure

![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Microsoft Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)

## Sobre o Projeto

Este projeto foi desenvolvido durante o curso Microsoft Azure Cloud Native 2026, ministrado pela DIO (Digital Innovation One).

O objetivo foi criar uma solução para armazenar e gerenciar dados de um e-commerce na nuvem, utilizando Azure SQL Server e Azure Blob Storage, com foco em escalabilidade, segurança e eficiência.

Foi o meu 1° contato prático com a plataforma Azure, além do aprendizado básico na interface, permitindo integrar armazenamento de dados, upload de imagens e listagem dinâmica de produtos com Streamlit.

## Funcionalidades

- Cadastro de produtos com:
  - Nome
  - Preço
  - Descrição
  - Upload de imagem (armazenada no Azure Blob Storage)
- Listagem de produtos cadastrados
- Tratamento de erros com `traceback` para depuração e exibição detalhada
- Interface web interativa criada com Streamlit

## 📷 Screenshots do Sistema

### Tela de Cadastro de Produtos
<img src="img/cadastroProdutos.png" width="50%" />

### Tela de Listagem de Produtos
<img src="img/listagemProdutos.png" width="50%" />

## Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|-----------|
| Python | Lógica de backend e integração com Azure |
| Streamlit | Criação da interface web interativa |
| Azure SQL Server | Armazenamento de dados estruturados |
| Azure Blob Storage | Armazenamento de imagens de produtos |
| dotenv | Gestão de variáveis de ambiente para segurança |

## Aprendizados

- Integração de Python com Azure SQL: Aprendi a conectar, inserir e recuperar dados do SQL Server.
- Gerenciamento de arquivos no Azure Blob: Criação de containers, upload e geração de URLs públicas.
- Tratamento de exceções e depuração: Uso do módulo `traceback` para capturar erros detalhados.
- Streamlit para dashboards interativos: Criação de formulários de cadastro e visualização de produtos de forma dinâmica.

## Autora

Milla Regina Lopes Vieira - [LinkedIn](https://www.linkedin.com/in/milla-regina-468020206/)