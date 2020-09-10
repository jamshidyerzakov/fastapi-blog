from fastapi import FastAPI

app = FastAPI()


@app.get("/home")  # handler at route "/home"
def home():
    return {"details": "You are at home!"}
