from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {
        "message": "Hello index",
    }


@app.get("/hello")
def hello(name: str = "world"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": email.email,
    }


@app.post("/calc/add")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


@app.get("/items/")
def list_items():
    return [
        "item1",
        "item2",
    ]


@app.get("/items/latest/")
def get_lastest_item():
    return {
        "item": {"id": "0", "name": "latest"}
    }


@app.get("/items/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id,
        },
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
