from fastapi import FastAPI,HTTPException
import json
from pydantic import BaseModel

app = FastAPI()

ARCHIVO = 'libros.json'
class Libro(BaseModel):
    titulo: str
    autor: str
    anio: int

def leer():
    with open(ARCHIVO, encoding="utf-8") as f:
        return json.load(f)


def guardar(libros):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(libros, f, indent=2, ensure_ascii=False)

@app.get("/")
def inicio():
    return {"mensaje": "Hola, FastAPI"}

@app.get("/libros")
def listar():
    return leer()

@app.get("/libros/{id}")
def buscar(id: int):
    for libro in leer():
        if libro["id"] == id:
            return libro
    raise HTTPException(status_code=404, detail="Ese libro no existe")

@app.post("/libros")
def agregar(libro: Libro):
    libros = leer()
    id_mas_alto = 0
    for a in libros:
        if a["id"] > id_mas_alto:
            id_mas_alto = a["id"]
    nuevo = {
        "id": id_mas_alto + 1,
        "titulo": libro.titulo,
        "autor": libro.autor,
        "anio": libro.anio,
    }
    libros.append(nuevo)
    guardar(libros)
    return nuevo

@app.put("/libros/{id}")
def editar(id: int, datos: Libro):
    libros = leer()
    for libro in libros:
        if libro["id"] == id:
            libro["titulo"] = datos.titulo
            libro["autor"] = datos.autor
            libro["anio"] = datos.anio
            guardar(libros)
            return libro
    raise HTTPException(status_code=404, detail="Ese libro no existe")

@app.delete("/libros/{id}")
def borrar(id: int):
    libros = leer()
    for libro in libros:
        if libro["id"] == id:
            libros.remove(libro)
            guardar(libros)
            return {"mensaje": "Libro borrado"}
    raise HTTPException(status_code=404, detail="Ese Libro no existe")