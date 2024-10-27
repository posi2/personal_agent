from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from UI.home_page import content
from module.code_generator import CodeGenerator

app = FastAPI()

@app.get("/")
def read_root():
     return HTMLResponse(content=content)

@app.post("/code_generator")
def generate_code(request):
     return CodeGenerator(request)._generate_code()