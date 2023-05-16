from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional

app = FastAPI()


class Libro(BaseModel):
    titulo:str
    autor:str
    pagina:int
    editorial:Optional [str]

@app.get("/")
def index():
    return {"message":"Hola Fastapi"}

@app.post("/libros")
def insertar_libro(libro:Libro):
    return{"mesagge":"el libro ha sido insertado"}




