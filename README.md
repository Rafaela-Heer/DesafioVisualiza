<h1 align="center"> 💫Visualiza API🔭</h1>

Microserviço em Python com FastAPI que consome a API da NASA (APOD - Astronomy Picture of the Day) e retorna os dados em formato JSON e em uma página web estilizada.
Feito exclusivamente para o desafio técnico para a vaga de estágio Visualiza.

## Funcionalidades
-  Acesso à imagem astronômica do dia da NASA(apod)
-  Endpoint JSON para integrar com outras aplicações(`apod`)
-  Página web com imagem, título e explicação (`/apod-web`)
-  Rota verificando o funcioamento da API (`/health`)
-  Containerização com Docker e Docker Compose

## Tecnologias

- Python 3.12
- FastAPI
- httpx
- Uvicorn
- Docker + Docker Compose
- API pública da NASA (APOD)

## ▶️ Como rodar o projeto com Docker

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/visualiza-api.git
cd visualiza-api
```

### 2. Coloque sua chave API da NASA no arquivo `.env`
```env
NASA_API_KEY=sua_chave_da_api
```
🔑 Você pode gerar sua chave gratuita aqui: https://api.nasa.gov/

### 3. Suba o container com Docker Compose
```bash
docker-compose up --build
```
A aplicação estará disponível em:
 http://localhost:8000

##  Rotas disponíveis

| Método | Rota         | Descrição                                        |
|--------|--------------|--------------------------------------------------|
| GET    | `/`          | Mensagem de boas-vindas                          |
| GET    | `/health`    | Verifica se a API está online                    |
| GET    | `/apod`      | Retorna os dados da imagem do dia em JSON       |
| GET    | `/apod-web`  | Exibe a imagem do dia em uma página estilizada  |
| GET    | `/docs`      | Interface interativa (Swagger UI)               |
| GET    | `/redoc`     | Documentação alternativa (ReDoc)                |

## Estrutura do Projeto
```
├── .github/
│ └── workflows/
├── src/
│ ├── init.py
│ └── main.py
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
└── requirements.txt
```

![Build Status](https://github.com/Rafaela-Heer/DesafioVisualiza/actions/workflows/main.yml/badge.svg)
