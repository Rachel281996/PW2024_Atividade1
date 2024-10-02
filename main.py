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

