from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
from fastapi.templating import Jinja2Template

from models.produtos_model import Produto
from repositories import produto_preço

produto_repo.criar_tabela()

app = FastAPI()
templates = Jinja2Templates(directory = "templates")
static = Jinja2Template(ditectory="static")

@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
def get_contato(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/post_contato")
def post_contato(
    nome: str = Form(...), 
    descricao: str = Form(...), 
    estoque: str = Form(...), 
    preco: str = Form(...)):
    categoria: str = Form(...)):
    produto =produto( none,nome, descricao, estoque,preco,categoria)
    produto = produto_repo.inserir(produto)
    return RedirectResponse("/cadastro_recebido", 303)

@app.get("/contato_recebido")
def get_cadastro_recebido(request: Request):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request})
