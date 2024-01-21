from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from contextlib import asynccontextmanager
from typing import Annotated, List
from dotenv import dotenv_values
from models import ToDoItem

from azure.cosmos.aio import CosmosClient
from azure.cosmos import PartitionKey


config = dotenv_values(".env")

COSMOS_DATABASE_NAME = "todo-db"
COSMOS_CONTAINER_NAME = "todo-items"


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.cosmos_client = CosmosClient(config["COSMOS_URI"], credential=config["COSMOS_KEY"])
    app.todo_database = await app.cosmos_client.create_database_if_not_exists(COSMOS_DATABASE_NAME)
    app.todo_items_container = await app.todo_database.create_container_if_not_exists(
        id=COSMOS_CONTAINER_NAME, partition_key=PartitionKey(path="/id")
    )
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/insert", response_model=ToDoItem)
async def create_todo(todo_item: Annotated[ToDoItem, Body()]):
    await app.todo_items_container.create_item(jsonable_encoder(todo_item))
    return todo_item

@app.get("/listall", response_model=List[ToDoItem])
async def list_todos():
    todos = [todo async for todo in app.todo_items_container.read_all_items()]
    return todos

