from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from logic import spin_reels

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

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
                    with open(path, "r", encoding=encoding) as file:
                        return file.read()

    return "<html><body><h1>404 - Файл не найден</h1></body></html>"

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)