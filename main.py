from fastapi import FastAPI, Response, Request, Path, Query, Body
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse, JSONResponse, RedirectResponse
import uvicorn
from fastapi.staticfiles import StaticFiles


def read_html_file(file_name):
    encodings = ['utf-8', 'cp1251', 'iso-8859-1', 'windows-1252']       
    for encoding in encodings:
        with open(file_name, "r", encoding=encoding) as file:
            return file.read()

app = FastAPI()

@app.get("/")
def root():
    htmldata = read_html_file("frontend\\index.html")
    return HTMLResponse(htmldata)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)