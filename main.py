from typing import Union

from fastapi import FastAPI

from chat_bot import chat

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/chat")
def read_item(message: str):
    return chat(message)
