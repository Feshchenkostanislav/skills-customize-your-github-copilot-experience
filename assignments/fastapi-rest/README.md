# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework. Students will implement endpoints, request/response models, and run a local server.

## 📝 Tasks

### 🛠️ Implement a REST API

#### Description
Create a small REST API using FastAPI. The API should support listing items, retrieving a single item by id, and creating new items. Use Pydantic models for request/response validation.

#### Requirements
Completed program should:

- Provide an endpoint `GET /items` that returns a list of items.
- Provide an endpoint `GET /items/{id}` that returns a single item or `404` if not found.
- Provide an endpoint `POST /items` that accepts an item model and adds it to an in-memory store.
- Use Pydantic models for input/output validation.
- Include a `main()` or `if __name__ == '__main__'` entry so the app can be run with `python starter-code.py` (uses `uvicorn`).
- Include a `requirements.txt` listing `fastapi` and `uvicorn`.
- Keep the implementation simple and well-structured (split to functions where appropriate).

Example usage (manual):

```
# Start the server
python starter-code.py

# List items
curl http://127.0.0.1:8000/items

# Create an item
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"id":1,"name":"Pen","description":"Blue pen"}'
```

Starter code: `starter-code.py`
