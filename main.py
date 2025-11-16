from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))  # Render will inject the PORT value
    uvicorn.run("main:app", host="0.0.0.0", port=port)
