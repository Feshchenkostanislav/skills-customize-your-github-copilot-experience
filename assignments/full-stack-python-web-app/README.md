# 📘 Assignment: Full-Stack Python Web App

## 🎯 Objective

Build a simple FastAPI backend and a connected HTML/JavaScript frontend to learn how client code and server code work together in a full-stack Python web app.

## 📝 Tasks

### 🛠️ Build the API

#### Description
Create a FastAPI app with endpoints for listing items, retrieving a single item, and adding new items. Use Pydantic models for validation and keep the data in an in-memory store.

#### Requirements
Completed program should:

- Provide an endpoint `GET /items` that returns a list of items.
- Provide an endpoint `GET /items/{id}` that returns a single item or `404` if not found.
- Provide an endpoint `POST /items` that accepts a JSON body and adds the item to an in-memory store.
- Use a Pydantic model for item validation.
- Add CORS middleware so the frontend page can request data from the backend.
- Include a `main()` or `if __name__ == '__main__'` entry so the app can be run with `python starter-code.py`.

Example usage:

```
python starter-code.py
```

### 🛠️ Create the frontend

#### Description
Build a `frontend.html` page that loads items from the API and lets the user add new items using JavaScript `fetch()` requests.

#### Requirements
Completed frontend should:

- Load items from `GET /items` and display them in a list.
- Provide a form to submit a new item with `id`, `name`, and `description`.
- Send the new item to `POST /items` and update the list after a successful response.
- Display error messages when item creation fails.
- Keep the frontend simple and focused on the API connection.

### 🛠️ Connect and test

#### Description
Run the backend server and open the frontend page to verify the full stack works together.

#### Requirements
Completed project should:

- Run the FastAPI backend locally at `http://127.0.0.1:8000`.
- Open `frontend.html` in the browser and successfully load items.
- Add at least two items through the frontend form and see them appear in the list.
- Confirm the item details are displayed correctly after creation.
