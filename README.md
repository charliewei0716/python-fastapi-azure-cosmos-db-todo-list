[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/charliewei0716/python-fastapi-azure-cosmos-db-todo-list?quickstart=1)

# Building a Todo List Application with Azure Cosmos DB and FastAPI in Python

This repository contains a Todo List application that demonstrates how to use [Azure Cosmos DB](https://learn.microsoft.com/zh-tw/azure/cosmos-db/introduction) as a backend database with a [FastAPI](https://fastapi.tiangolo.com/) service in Python. The application allows users to manage their todo items with CRUD operations.

## Features
- Set up the development environment and install the required Python libraries.
- Connect to Azure Cosmos DB using a KEY with the Python client.
- Create the necessary databases and containers using Python.
- Define the ToDoItem data model in FastAPI and write the CRUD API endpoints.

## Getting Started
1. Click on the **Open in GitHub Codespaces** above to open this repository in Codespaces.
2. Create a file named *.env* in the */src/* directory, and write your  `COSMOS_URI` and `COSMOS_KEY` into it.
3. Start the web app:
  ```
  uvicorn main:app --reload
  ```

## Blog Post
For more detailed explanations and insights about this project, check out my blog post:
