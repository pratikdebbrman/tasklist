from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pathlib import Path
import json

app = FastAPI()

# Load the JSON data
with open('pune_prj1.json') as f:
    village_data = json.load(f)

@app.get("/", response_class=HTMLResponse)
async def index():
    html_content = Path("index.html").read_text()
    return HTMLResponse(content=html_content)

@app.get("/data")
async def get_data():
    return JSONResponse(content=village_data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
