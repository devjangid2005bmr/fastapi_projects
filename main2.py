from fastapi import FastAPI

app = FastAPI(
    title = "hello world",
    description = "this is the world"
)


@app.get("/")
def home():
    return {
        "message":"hello how are you"
    }