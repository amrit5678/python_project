from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    return templates.TemplateResponse("result.html", {"request": request, "contents": contents})


@app.get("/")
async def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

