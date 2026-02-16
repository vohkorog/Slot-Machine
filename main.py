from fastapi import FastAPI, Response, Request, Path, Query, Body
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse, JSONResponse, RedirectResponse
import uvicorn
from fastapi.staticfiles import StaticFiles
import os
from logic import spin_reels


def read_html_file(file_name):
    encodings = ['utf-8', 'cp1251', 'iso-8859-1', 'windows-1252']      
    possible_paths = [
        file_name,
        os.path.join("frontend", file_name),
        os.path.join("static", file_name)
    ] 
    for path in possible_paths:
        if os.path.exists(path):
            for encoding in encodings:
                try:
                    with open(path, "r", encoding=encoding) as file:
                        return file.read()
                except UnicodeDecodeError:
                    continue
                except FileNotFoundError:
                    continue
    
    # Если ничего не нашли, возвращаем простой HTML с ошибкой
    return "<html><body><h1>404 - Файл не найден</h1></body></html>"

app = FastAPI()

@app.get("/")
def root():
    htmldata = read_html_file("index.html")
    return HTMLResponse(htmldata)

@app.post("/api/spin")
async def spin():

    result = spin_reels()
    return JSONResponse({
            "success": True,
            "reels": result["reels"],
            "message": result["message"],
            "win": result["win"]
        })

@app.get("/health")
def health_check():
    return {"status": "сервер работает"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)