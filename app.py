from fastapi import FastAPI
from fastapi.responses import HTMLResponse
# from ui.home_page import content
from prajna.code_generator.code_generator import CodeGenerator
from starlette.requests import Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="ui")

app = FastAPI()

     # @app.get("/")
     # async def read_root():
     #      return HTMLResponse(content=content)

@app.post("/code_generator")
async def generate_code(request):
     return CodeGenerator(request)._generate_code()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Here you can pass dynamic data to your template if needed
    return templates.TemplateResponse("index.html", {"request": request})