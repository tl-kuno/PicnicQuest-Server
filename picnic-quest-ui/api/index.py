from fastapi import FastAPI
app = FastAPI


@app.get("/")
def read_root():
    return {"message": "Server is up and running"}
