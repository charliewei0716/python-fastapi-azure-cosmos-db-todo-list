[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/charliewei0716/python-fastapi-azure-cosmos-db-todo-list?quickstart=1)

# Building a Todo List Application with Azure Cosmos DB and FastAPI in Python

This repository hosts a Todo List application that demonstrates the integration of [Azure Cosmos DB](https://learn.microsoft.com/zh-tw/azure/cosmos-db/introduction) as a backend database with a [FastAPI](https://fastapi.tiangolo.com/) service in Python. It offers a simple interface for users to manage their tasks with Create, Read, Update, and Delete (CRUD) operations.

## Features
- Set up the development environment and install the required Python libraries.
- Connect to Azure Cosmos DB using a KEY with the Python client.
- Create the necessary databases and containers using Python.
- Definition of the ToDoItem data model within FastAPI and implementation of the CRUD API endpoints.

## Getting Started
1. Click on the **Open in GitHub Codespaces** above to open this repository in Codespaces.
2. Within the Codespaces environment, navigate to the */src/* directory and create a *.env* file. Populate it with your Azure Cosmos DB URI and KEY like so:
  ```
  COSMOS_URI = "your_cosmos_db_uri"
  COSMOS_KEY = "your_cosmos_db_key"
  ```
3. Launch the web app by running the following commands:
  ```
  cd src/ &&
  uvicorn main:app --reload
  ```

## Blog Post
For more detailed explanations and insights about this project, check out my blog post:
