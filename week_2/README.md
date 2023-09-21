# ToDo App API

The ToDo App API is a Django REST framework-based web service that allows users to manage their tasks and to-dos efficiently. It provides endpoints for creating, reading, updating, and deleting tasks.

## Table of Contents

- [ToDo App API](#todo-app-api)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [Authentication](#authentication)
    - [JWT(JSON Web Token) - split file](https://github.com/AGIZA-eg/alx-pre_course/blob/master/week_2/Learn_JWT.md)
  - [Endpoints](#endpoints)
    - [Get all tasks:](#get-all-tasks)
    - [Create a new task:](#create-a-new-task)
    - [Request Body:](#request-body)
    - [Get a single task by ID:](#get-a-single-task-by-id)
    - [Update a task by ID:](#update-a-task-by-id)
    - [Delete a task by ID:](#delete-a-task-by-id)

## Features

- Create new tasks.
- Retrieve a list of all tasks.
- Retrieve a single task by ID.
- Update task details.
- Delete a task.
- Search for tasks by title.
- Filter tasks by status (incomplete or complete).

## Project Structure

The project follows a standard Django project structure:

## Installation

Follow these steps to set up the project locally:

1. Clone the repository to your local machine:
git clone https://github.com/

2. Navigate to the project directory:
cd project 

3. Apply database migrations:
python manage.py migrate

4. Create a superuser to access the Django admin panel:
python manage.py createsuperuser

5. Start the development server:
python manage.py runserver


## Configuration

You can configure the project settings in the `ToDoApp/settings.py` file. This includes database settings, authentication settings, and more.

## Usage

1. Access the Django admin panel to manage users, tasks, and authentication tokens:
http://localhost:8000/admin/

2. Use the provided API endpoints to interact with tasks.

### Authentication

Authentication is required for most API endpoints. You can obtain an authentication token by sending a POST request to:

POST http://localhost:8000/api/token/


Request Body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```


Authorization: Bearer <access_token>


## Endpoints
Here are the available API endpoints:

### Get all tasks:

```bash

GET http://localhost:8000/api/todos/

```

### Create a new task:

```bash

POST http://localhost:8000/api/todos/

```

### Request Body:

```json
{
  "user": 1,
  "title": "Task Title",
  "description": "Task Description",
  "complete": false
}

```

### Get a single task by ID:

```bash

GET http://localhost:8000/api/todos/<task_id>/

```
### Update a task by ID:

```bash

PUT http://localhost:8000/api/todos/<task_id>/


```
### Delete a task by ID:

```bash

DELETE http://localhost:8000/api/todos/<task_id>/

```
