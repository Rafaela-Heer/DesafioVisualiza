from fastapi import FastAPI, HTTPException
import httpx
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

@app.get("/")
def root():
    return {"message" : "Bem-vindo à Visualiza API!"}

@app.get("/health")
def health():
    return {"status": "ok"}

from fastapi.responses import HTMLResponse

@app.get("/apod")
async def get_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/apod-web", response_class=HTMLResponse)
async def get_apodweb():
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()

            title = data.get("title", "Image of the day:")
            explanation = data.get("explanation", "No details about the image")
            image_url = data.get("hdurl") or data.get("url")

            html_content = f"""
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <title>{title}</title>
                <link href="https://fonts.googleapis.com/css2?family=Rubik&display=swap" rel="stylesheet">
                <style>
                    body {{
                        font-family: 'Rubik', sans-serif;
                        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                        color: #fff;
                        margin: 0;
                        padding: 0;
                    }}
                    .container {{
                        max-width: 900px;
                        margin: 3rem auto;
                        background-color: rgba(255, 255, 255, 0.05);
                        padding: 2rem;
                        border-radius: 15px;
                        box-shadow: 0 0 20px rgba(0,0,0,0.3);
                    }}
                    img {{
                        width: 100%;
                        border-radius: 10px;
                        margin-bottom: 1.5rem;
                    }}
                    h1 {{
                        margin-top: 0;
                        font-size: 2.2rem;
                        color: #fff;
                    }}
                    p {{
                        font-size: 1.1rem;
                        line-height: 1.6;
                    }}
                    @media (max-width: 600px) {{
                        .container {{
                            margin: 1rem;
                            padding: 1rem;
                        }}
                        h1 {{
                            font-size: 1.5rem;
                        }}
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>{title}</h1>
                    <a href="{image_url}" target="_blank">
                        <img src="{image_url}" alt="{title}" title="Clique para ampliar">
                    </a>
                    <p>{explanation}</p>
                </div>
            </body>
            </html>
            """

            return HTMLResponse(content=html_content)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
