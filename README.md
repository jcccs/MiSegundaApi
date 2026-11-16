# 📚 API REST de Gestión de Libros

API desarrollada con **FastAPI** y **Pydantic** que permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre un catálogo de libros[cite: 1].

## 🚀 Tecnologías utilizadas

* **Python 3.10+**
* **FastAPI** - Framework web rápido y moderno para construir APIs.
* **Pydantic** - Validación de datos mediante modelos tipados.
* **Uvicorn** - Servidor ASGI para ejecutar la aplicación.

## 📌 Endpoints disponibles

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| `GET` | `/` | Ruta de inicio / bienvenida de la API[cite: 1]. |
| `GET` | `/libros` | Lista todos los libros registrados[cite: 1]. |
| `POST` | `/libros` | Agrega un nuevo libro al catálogo[cite: 1]. |
| `GET` | `/libros/{id}` | Busca y devuelve un libro específico por su `id`[cite: 1]. |
| `PUT` | `/libros/{id}` | Edita los datos de un libro existente según su `id`[cite: 1]. |
| `DELETE` | `/libros/{id}` | Elimina un libro del catálogo según su `id`[cite: 1]. |

## 📦 Estructura de datos (Modelo)

Para crear o actualizar un libro (`POST` / `PUT`), la API espera un cuerpo en formato JSON con la siguiente estructura:

```json
{
  "titulo": "Un mundo feliz",
  "autor": "Aldous Huxley",
  "año": 1932
}
