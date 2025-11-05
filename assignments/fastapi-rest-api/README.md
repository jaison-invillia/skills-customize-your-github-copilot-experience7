# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework in Python. You will create a simple task management API that supports creating, reading, updating, and deleting tasks, while implementing proper HTTP methods and status codes.

## 📝 Tasks

### 🛠️	Create Basic API Structure

#### Description
Set up a FastAPI application with basic endpoints to manage a collection of tasks. Each task should have an id, title, description, and completion status.

#### Requirements
Completed program should:

- Install and import FastAPI and uvicorn
- Create a FastAPI application instance
- Define a Task model using Pydantic BaseModel
- Implement an in-memory list to store tasks
- Include a root endpoint (GET /) that returns a welcome message


### 🛠️	Implement CRUD Operations

#### Description
Create endpoints that allow full CRUD (Create, Read, Update, Delete) operations for tasks following REST conventions.

#### Requirements
Completed program should:

- Implement POST /tasks to create a new task
- Implement GET /tasks to retrieve all tasks
- Implement GET /tasks/{task_id} to retrieve a specific task
- Implement PUT /tasks/{task_id} to update an existing task
- Implement DELETE /tasks/{task_id} to delete a task
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Handle errors gracefully with proper error messages


### 🛠️	Add Data Validation and Documentation

#### Description
Enhance your API with input validation and explore FastAPI's automatic documentation features.

#### Requirements
Completed program should:

- Use Pydantic models to validate request data
- Ensure task titles are not empty and have a maximum length
- Validate that task IDs exist before updating or deleting
- Test all endpoints using the auto-generated Swagger UI at /docs
- Include at least 3 example tasks when the server starts
