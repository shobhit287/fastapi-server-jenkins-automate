from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
def server_status():
    return {"message": "Server running 1.6"}