from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from starlette.requests import Request


app = FastAPI()
templates = Jinja2Templates(directory = "templates")


static = Jinja2Templates(directory = "static")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)

from fastapi import Request

@app.get("/cadastro")
async def cadastro_produto(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

from fastapi import Request

@app.get("/cadastro")
async def cadastro_produto(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})


from fastapi import Form, Request
from fastapi.responses import RedirectResponse

@app.post("/post_cadastro")
async def post_cadastro(
    nome: str = Form(...),
    descricao: str = Form(...),
    estoque: int = Form(...),
    preco: float = Form(...),
    categoria: str = Form(...)
):
    # Aqui você pode processar os dados recebidos, como armazenar em um banco de dados
    print(f"Produto cadastrado: {nome}, {descricao}, {estoque}, {preco}, {categoria}")
    
    # Após o processamento, redireciona para a página inicial
    return RedirectResponse(url="/", status_code=303)


