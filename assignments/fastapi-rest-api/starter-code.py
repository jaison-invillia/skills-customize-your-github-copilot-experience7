# FastAPI REST API - Starter Code
# Student Name: _________________
# Date: _________________

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# TODO: Create FastAPI app instance


# TODO: Define Task model using Pydantic BaseModel
# Hint: Include fields for id (int), title (str), description (str), and completed (bool)


# TODO: Create an in-memory list to store tasks
tasks = []


# TODO: Implement root endpoint
# GET / - Returns a welcome message


# TODO: Implement CRUD endpoints below

# POST /tasks - Create a new task


# GET /tasks - Get all tasks


# GET /tasks/{task_id} - Get a specific task


# PUT /tasks/{task_id} - Update a task


# DELETE /tasks/{task_id} - Delete a task


# To run this API, use the command:
# uvicorn starter-code:app --reload
