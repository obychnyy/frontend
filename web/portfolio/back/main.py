from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
fro

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"]
)

OUTPUT_DIR = "templates"

class ModuleData(BaseModel):
    title: str
    description: str
    code1: str
    code2: str | None = None
    
@app.post("/sreate-module")
def create_module(data: ModuleData):
    folder = f"{OUTPUT_DIR}/{data.title.replace(' ', '_')}"
    os.makedirs(folder, exist_ok=True)
    html_path = f"{folder}/index.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{data.title}</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<h1>{data.title}</h1>
<p>{data.description}</p>

<pre><code>{data.code1}</code></pre>
{"<pre><code>" + data.code2 + "</code></pre>" if data.code2 else ""}
</body>
</html>
""")

    css_path = f"{folder}/styles.css"
    with open(css_path, "w") as f:
        f.write("body { font-family: Arial; padding: 40px; }")

    return {"message": "success", "url": f"/{folder}/index.html"}